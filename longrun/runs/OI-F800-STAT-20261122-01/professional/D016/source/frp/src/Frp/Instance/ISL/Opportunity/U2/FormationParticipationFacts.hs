{-# LANGUAGE DeriveAnyClass #-}
{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE NoOverloadedLists #-}
{-# LANGUAGE OverloadedStrings #-}
-- | 原F已作出的参与/决定小事实；由原writer保存，Clusters只有限承接。
module Frp.Instance.ISL.Opportunity.U2.FormationParticipationFacts where
import Control.DeepSeq (NFData)
import Data.Int (Int64)
import Data.Text (Text)
import GHC.Generics (Generic)
import Frp.Apt.Bson (ToBSON,FromBSON)
import Frp.Instance.ISL.Opportunity.U2.ThinNodeResults (ThinDefinition)

data FormationDecisionMethod=AdmittedCompleteLinkContradictionV1 deriving (Eq,Show,Enum,Bounded)
data FormationDecisionScope=WholeCandidateCombination deriving (Eq,Show,Enum,Bounded)
data RejectionCoordinate=RejectionDistance | RejectionDirection | RejectionTurnType | RejectionBend
 deriving (Eq,Ord,Show,Enum,Bounded)
data RejectionSupportState=EffectiveRejection | ExplicitlyCorrected | UnresolvedCorrection
 | InvalidatedBasis | CurrentBasisOutsideOriginalDuty deriving (Eq,Ord,Show,Enum,Bounded)
data ParticipationSubject=ParticipationApplicable | ParticipationInvalidated deriving (Eq,Show,Enum,Bounded)
data AlternativeRelationKind=CandidateOverlap | CandidateCoveredBy deriving (Eq,Show,Enum,Bounded)
data FormationNumber=FormationNumber {formationNumber :: !Double}
 deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data FormationInteger=FormationInteger {formationInteger :: !Int64}
 deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data ParticipationMember=ParticipationMember
 { participationObject :: !Text,participationTurn :: !ThinDefinition,participationSource :: !ThinDefinition
 , participationActual :: !Int64,participationConfirmation :: !Int64,participationMemberKnown :: !Int64 }
 deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data FormationPoint=FormationPoint
 { formationPointActual :: !Int64,formationPointPrice :: !Double,formationPointKnown :: !Int64
 , formationPointClock :: ![FormationNumber],formationPointClockKnown :: ![FormationInteger] }
 deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data FormationOperand=FormationOperand
 { formationOperandMember :: !ParticipationMember,formationOperandNumber :: ![FormationNumber]
 , formationOperandCategory :: ![FormationInteger],formationOperandPoints :: ![FormationPoint]
 , formationOperandKnown :: !Int64 }
 deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data FormationSupport=FormationSupport
 { supportLeft :: !Text,supportLeftTurnLife :: !Text,supportRight :: !Text,supportRightTurnLife :: !Text
 , supportCoordinate :: !Int64,supportState :: !Int64,supportReason :: !Int64
 , supportRejectedAt :: !ThinDefinition,supportChangedAt :: !ThinDefinition,supportPreviousFact :: ![ThinDefinition]
 , supportOperands :: ![FormationOperand],supportKnown :: !Int64 }
 deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data FormationAlternative=FormationAlternative
 { alternativeOwner :: !ThinDefinition,alternativeLeft :: !ThinDefinition,alternativeRight :: !ThinDefinition
 , alternativeKind :: !Int64,alternativeBridge :: ![ParticipationMember],alternativeKnown :: !Int64 }
 deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
-- 期外成功输入只限制相交支撑的当前用途；不改写原F冻结的决定。
data FormationOutsideNotice=FormationOutsideNotice
 { outsideLeft :: !Text,outsideLeftTurnLife :: !Text,outsideRight :: !Text,outsideRightTurnLife :: !Text
 , outsideCoordinate :: !Int64,outsideObject :: !Text,outsideActual :: !Int64,outsideKind :: !Int64
 , outsideNumber :: ![FormationNumber],outsideTurn :: ![ThinDefinition],outsideKnown :: !Int64 }
 deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
data FormationParticipation=FormationParticipation
 { participationAdmission :: !ThinDefinition,participationAdmissionKnown :: !Int64
 , participationCandidate :: !ThinDefinition,participationMembers :: ![ParticipationMember]
 , participationQuestionAnchor :: !Double,participationQuestionDeadline :: !Double,participationQuestionRevisionEnd :: !Double
 , participationDeadline :: !Double,participationRevisionEnd :: !Double,participationHandoffEnd :: !Double
 , participationDecisionMethod :: !Int64,participationDecisionScope :: !Int64,participationSubject :: !Int64
 , participationHistoryComplete :: !Int64,participationDutyClosed :: !Int64
 , participationSupports :: ![FormationSupport],participationAlternatives :: ![FormationAlternative]
 , participationOutsideNotifications :: ![FormationOutsideNotice],participationInputConflict :: !Int64,participationDecisionKnown :: !Int64 }
 deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
-- | 原Cluster安装处给出的实际使用与结构处分，无独立Life。
data CandidateUseDisposition=CandidateUseDisposition
 { candidateUseSource :: !ThinDefinition,candidateUseOriginalHost :: !ThinDefinition
 , candidateUseAt :: !ThinDefinition,candidateUseKnown :: !Int64
 , candidateUseRetained :: ![ParticipationMember],candidateUseExcluded :: ![ParticipationMember]
 , candidateUseUntil :: !Double }
 deriving (Eq,Show,Generic,NFData,ToBSON,FromBSON)
factCode :: Enum a => a -> Int64
factCode=fromIntegral . fromEnum

-- 保存/输入边界检查，不重算Pair或重建候选。
validateFormationParticipation :: Int64 -> FormationParticipation -> Either Text ()
validateFormationParticipation known f=do
 require (participationDecisionMethod f==0 && participationDecisionScope f==0) "未知原F正式决定方法/范围"
 require (participationSubject f `elem` [0,1] && participationHistoryComplete f `elem` [0,1] && participationDutyClosed f `elem` [0,1] && participationInputConflict f `elem` [0,1]) "未知原F参与状态"
 require (participationAdmissionKnown f<=participationDecisionKnown f && participationDecisionKnown f<=known) "原F参与知识倒序/未来"
 require (all finite [participationQuestionAnchor f,participationDeadline f,participationRevisionEnd f,participationHandoffEnd f]
   && participationDeadline f<=participationQuestionDeadline f && participationRevisionEnd f<=participationQuestionRevisionEnd f
   && participationDeadline f<=participationRevisionEnd f && participationRevisionEnd f<=participationHandoffEnd f) "原F参与责任被延长或数值非法"
 mapM_ (\s->do
   require (supportCoordinate s `elem` [0..3] && supportState s `elem` [0..4] && supportReason s `elem` [0..3]) "未知正式反证坐标/状态/原因"
   require (length (supportOperands s)==2 && supportKnown s<=known && length (supportPreviousFact s)<=1) "正式反证端点/知识/前驱非法"
   mapM_ (\o->do
    require (formationOperandKnown o<=known && length (formationOperandNumber o)<=1 && length (formationOperandCategory o)<=1
      && all (finite . formationNumber) (formationOperandNumber o)) "正式反证操作数非法"
    mapM_ (\p->require (finite (formationPointPrice p) && formationPointKnown p<=known && length (formationPointClock p)<=1
      && length (formationPointClockKnown p)<=1 && all (finite . formationNumber) (formationPointClock p)
      && all ((<=known) . formationInteger) (formationPointClockKnown p)) "正式反证原点非法") (formationOperandPoints o)) (supportOperands s)) (participationSupports f)
 mapM_ (\n->require (outsideCoordinate n `elem` [0..3] && outsideKind n `elem` [0..2] && outsideKnown n<=known
   && length (outsideNumber n)<=1 && all (finite . formationNumber) (outsideNumber n) && length (outsideTurn n)<=1)
   "期外相交通知数值/知识/分类非法") (participationOutsideNotifications f)
 mapM_ (\e->require (alternativeKind e `elem` [0,1] && not (null (alternativeBridge e)) && alternativeKnown e<=known) "候选直接关系缺固定桥或含未来知识") (participationAlternatives f)
 where
  require yes message=if yes then Right () else Left message
  finite x=not (isNaN x || isInfinite x)
