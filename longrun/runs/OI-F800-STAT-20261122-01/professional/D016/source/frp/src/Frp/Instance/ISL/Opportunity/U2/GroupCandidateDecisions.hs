{-# LANGUAGE NoOverloadedLists #-}
{-# LANGUAGE OverloadedStrings #-}
-- | 在原F成功演化中解析Required坐标；不把Withdrawn当正式拒绝。
module Frp.Instance.ISL.Opportunity.U2.GroupCandidateDecisions where
import Data.List (find)
import Data.Maybe (mapMaybe,maybeToList)
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import Frp.Instance.ISL.Opportunity.U2.Types
import Frp.Instance.ISL.Opportunity.U2.Episode (CalendarClockValue(..))
import Frp.Instance.ISL.Opportunity.U2.BoundedRelations
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateTypes
import Frp.Instance.ISL.Opportunity.U2.FormationParticipationFacts
import qualified Frp.Instance.ISL.Opportunity.U2.ThinNodeResults as Thin

captureParticipationMember t=ParticipationMember (groupTurnObject t) (Thin.definition (groupTurnRef t))
 (Thin.definition (groupTurnSource t)) (groupTurnActual t) (groupTurnConfirmation t) (groupTurnKnown t)
participationMemberKey p=(participationObject p,Thin.definitionLife (participationTurn p))
supportKey s=((supportLeft s,supportLeftTurnLife s),(supportRight s,supportRightTurnLife s),supportCoordinate s)
formationOperand coordinate t=FormationOperand (captureParticipationMember t) numbers category points known
 where
  clock=groupTurnClock t;g=groupTurnGeometry t
  numbers=case coordinate of RejectionDistance->maybe [] (pure . FormationNumber . groupClockValue) clock;_->[]
  category=map FormationInteger $ case coordinate of
   RejectionDirection->maybe [] (pure . directionCode) (groupTurnDirection t)
   RejectionTurnType->maybe [] (pure . factCode) (groupTurnType t)
   _->[]
  points=case coordinate of
   RejectionBend->mapMaybe id [point <$> geometryPKnown g <*> geometryP g,Just (point (geometryTKnown g) (geometryT g)),Just (point (geometryCKnown g) (geometryC g))]
   _->[]
  point k (actual,price,c)=FormationPoint actual price k
   (map (FormationNumber . clockValue) (maybeToList c)) (map (FormationInteger . clockValueKnownFrom) (maybeToList c))
  known=maximum (groupTurnKnown t:case coordinate of
   RejectionDistance->map groupClockKnown (maybeToList clock)
   RejectionBend->concat [[formationPointKnown p]++map formationInteger (formationPointClockKnown p) | p<-points]
   _->[])
  directionCode DirectionUp=0;directionCode DirectionDown=1

-- 完整当前支撑按有限pair/坐标归约；旧发生由原writer保存。
-- Handoff retains the legacy 18-Delta tail after revision duty. At the default
-- observation=6 this is the original anchor+30Delta; wider observation shifts
-- all three ordered duties without relaxing the storage invariant.
resolveFormationDecisionCorrections reference method material question body old=
 case old >>= candidateParticipation of
  Nothing->FormationParticipation ref (materialKnown material) ref (map (captureParticipationMember . fst) (candidateMembers body))
   (questionAnchor question) (questionDeadline question) (questionRevisionEnd question)
   (candidateDeadline body) (candidateRevisionEnd body) (min (questionRevisionEnd question+18*groupDelta method) (candidateRevisionEnd body+18*groupDelta method))
   (factCode AdmittedCompleteLinkContradictionV1) (factCode WholeCandidateCombination)
   (factCode subject) 1 (factCode closed) [] [] [] 0 (materialKnown material)
  Just before | materialProgress material>participationRevisionEnd before->before {participationCandidate=ref,participationDutyClosed=1,participationDecisionKnown=materialKnown material}
  Just before->before {participationCandidate=ref,participationDeadline=min (participationDeadline before) (candidateDeadline body)
   ,participationRevisionEnd=min (participationRevisionEnd before) (candidateRevisionEnd body)
   ,participationHandoffEnd=min (participationHandoffEnd before) (candidateRevisionEnd body+18*groupDelta method)
   ,participationSubject=factCode subject,participationDutyClosed=factCode closed
   ,participationSupports=supports before,participationDecisionKnown=materialKnown material}
 where
  ref=Thin.definition reference
  subject=if any (groupTurnRetracted . fst) (candidateMembers body) then ParticipationInvalidated else ParticipationApplicable
  closed=materialScopeEnded material || materialProgress material>=candidateRevisionEnd body
  turns=M.fromList [(refLife (groupTurnRef t),t) | (t,_)<-candidateMembers body]
  supports before=M.elems $ foldl update (M.fromList [(supportKey s,s) | s<-participationSupports before])
   [(p,c,v) | p<-candidatePairs body,(c,v)<-zip [RejectionDistance,RejectionDirection,RejectionTurnType,RejectionBend]
    [basisTime p,basisDirection p,basisType p,basisBend p]]
  update rows (pair,coordinate,verdict)=case (M.lookup (refLife (basisLeft pair)) turns,M.lookup (refLife (basisRight pair)) turns) of
   (Just a,Just b)->let
     key=(turnKey a,turnKey b,factCode coordinate);previous=M.lookup key rows
     operands=[formationOperand coordinate a,formationOperand coordinate b]
     status=if subject==ParticipationInvalidated then Just InvalidatedBasis else case verdict of
      CoordinateVeto SourceTurnWithdrawn->Just InvalidatedBasis
      CoordinateVeto _->Just EffectiveRejection
      CoordinateSupports->Just ExplicitlyCorrected
      CoordinateUnresolved _->Just UnresolvedCorrection
     install state reason rejection=FormationSupport (groupTurnObject a) (refLife (groupTurnRef a)) (groupTurnObject b) (refLife (groupTurnRef b))
      (factCode coordinate) (factCode state) reason rejection ref (maybe [] (pure . supportChangedAt) previous) operands
      (maximum (materialKnown material:map formationOperandKnown operands))
     next=case (status,previous) of
      (Just EffectiveRejection,prior)->Just (install EffectiveRejection (case verdict of CoordinateVeto r->factCode r;_->error "F反证分支")
       (case prior of Just s | supportState s/=factCode ExplicitlyCorrected->supportRejectedAt s;_->ref))
      (Just state,Just prior)->Just (install state
       (supportReason prior) (supportRejectedAt prior))
      _->Nothing
    in maybe rows (\s->M.insert key s rows) next
   _->rows

-- 比较实际决定含义，排除这次发行才分配的包装ref和处理前沿。
formationDecisionMeaning f=(participationAdmission f,participationMembers f,participationDeadline f,participationRevisionEnd f,
 participationHandoffEnd f,participationSubject f,participationHistoryComplete f,participationDutyClosed f,
 [(supportKey s,supportState s,supportReason s,supportOperands s) | s<-participationSupports f])

-- 双方最终准确ref在同一rows已分配后解析；旧真实关系不会随current overlap消失。
attachFormationAlternatives rows row=case candidateParticipation row of
 Nothing->row
 Just facts->row {candidateParticipation=Just facts {participationAlternatives=foldl add (participationAlternatives facts) desired}}
 where
  body=candidateBody row
  desired=[(other,kind) | (lives,kind)<-[(candidateOverlaps body,CandidateOverlap),(candidateCoveredBy body,CandidateCoveredBy)],
   life<-lives,Just other<-[find ((==life) . refLife . candidateReference) rows],candidateQuestion other==candidateQuestion row]
  add before (other,kind)
   | any (\edge->alternativeKind edge==factCode kind && Thin.definitionLife (alternativeLeft edge)==refLife (candidateReference row)
       && Thin.definitionLife (alternativeRight edge)==refLife (candidateReference other)) before=before
   | otherwise=let
      right=S.fromList (map (turnKey . fst) (candidateMembers (candidateBody other)))
      bridge=[captureParticipationMember t | (t,_)<-candidateMembers body,turnKey t `S.member` right]
     in if null bridge then before else before++[FormationAlternative (Thin.definition (candidateReference row))
       (Thin.definition (candidateReference row)) (Thin.definition (candidateReference other)) (factCode kind) bridge
       (max (candidateKnown row) (candidateKnown other))]
