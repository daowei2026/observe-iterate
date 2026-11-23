{-# LANGUAGE NoOverloadedLists #-}
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE TupleSections #-}
-- | 候选生命与稀疏发行的唯一owner。退出运行态不删除平台正式历史，
-- 不维护全部曾经候选或期外来源通知的永久逆向索引。
module Frp.Instance.ISL.Opportunity.U2.GroupCandidateEvolution where
import Control.Monad (forM,unless)
import Control.Monad.IO.Class (MonadIO,liftIO)
import Data.List (nub,sort,sortOn)
import Data.Maybe (mapMaybe)
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import Data.Text (Text)
import qualified Data.UUID as UUID
import qualified Data.UUID.V4 as UUID
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateDecisions
import Frp.Instance.ISL.Opportunity.U2.GroupCandidateTypes
import Frp.Instance.ISL.Opportunity.U2.GroupCandidatePairs
import Frp.Instance.ISL.Opportunity.U2.Source (finite)
import Frp.Instance.ISL.Opportunity.U2.Types

data CandidateState = CandidateState
  { activeCandidates :: !(M.Map CandidateKey CandidateOccurrence)
  , retiredParticipationObjects :: !(S.Set Text) -- ^ 只标记声明对象的current已有历史清退边界，不存旧候选或索引。
  }
  deriving (Eq,Show)
emptyCandidateState=CandidateState M.empty S.empty
candidateDependencies state=S.fromList [turnKey t | row<-M.elems (activeCandidates state),
  (t,_)<-candidateMembers (candidateBody row)]

-- | Bron–Kerbosch只在当次有限域内展开极大complete-link集合。
-- 相同对象之间无边；没有全子集表、跨年Turn域或打分赢家。
maximalCliques :: Ord a => S.Set a -> (a -> S.Set a) -> [S.Set a]
maximalCliques vertices adjacent=visit S.empty vertices S.empty
  where
    visit r p x
      | S.null p && S.null x=[r]
      | otherwise=walk (S.toAscList p) p x
      where
        walk [] _ _=[]
        walk (v:vs) remaining excluded=
          visit (S.insert v r) (S.intersection remaining (adjacent v)) (S.intersection excluded (adjacent v))
          ++walk vs (S.delete v remaining) (S.insert v excluded)

formationQuestions method view=nub $ concatMap groups anchors
  where
    material=pairMaterial view;turns=materialTurns material;u=materialProgress material;d=groupDelta method;observation=groupObservationDuration method
    clock key=groupClockValue <$> (M.lookup key turns >>= groupTurnClock)
    anchors=nub (sort (mapMaybe clock (S.toList (materialEnumerable material))))
    decision a b=pairDecision <$> M.lookup (pairKey a b) (pairBases view)
    groups a
      | u>a+observation=[]
      | otherwise=
        let vertices=S.filter (\key->maybe False (\c->a<=c && c<=a+observation) (clock key)) (materialEnumerable material)
            graph possible key=S.filter (\other->other/=key && case decision key other of
              Just PairPositive->True;Just PairUnresolved->possible;_->False) vertices
            cliques=maximalCliques vertices (graph False)++maximalCliques vertices (graph True)
        in [(FormationQuestion a (a+observation) (a+observation+6*d),S.toAscList members) | members<-cliques,
            S.size members>=2,minimum (mapMaybe clock (S.toList members))==a]

-- | 调用者先取得生产者成功的同拍最终材料；u=d/r先处理本次材料再关闭/退出。
-- 资格按旧r判，新Clock收紧到当前之前也发行此次合法最终观点一次。
advanceCandidates :: MonadIO m => GroupMethod -> PairView -> CandidateState
  -> m (Either Text (CandidateState,[CandidateOccurrence]))
advanceCandidates method view state
  | not affected = pure (Right (state,[]))
  | otherwise = case prepare of
    Left problem->pure (Left problem)
    Right (prior,wanted)->do
      identities<-forM wanted $ \key->case M.lookup key prior of
        Just row->pure (key,refLife (candidateReference row))
        Nothing->(key,) <$> opaque
      let lives=M.fromList identities
          initialBodies=M.fromList [(key,bodyFor key (M.lookup key prior)) | key<-wanted]
          linked=M.mapWithKey (link lives initialBodies) initialBodies
      rows<-forM wanted $ \key->do
        let body=linked M.! key;old=M.lookup key prior
        let preview r=resolveFormationDecisionCorrections r method material (fst key) body old
            unchanged=case old of
              Just before->candidateBody before==body && maybe False ((==formationDecisionMeaning (preview (candidateReference before))) . formationDecisionMeaning) (candidateParticipation before)
              _->False
        if unchanged then pure (key,old,False)
        else do
          rev<-opaque
          let reference=ExactRef "CommonPriceTurnGroupCandidates" "Candidate" (lives M.! key) rev
              row=CandidateOccurrence reference (candidateReference <$> old) (fst key)
                (materialKnown material) body (Just (preview reference))
          pure (key,Just row,True)
      let finalRows=[(k,fmap (attachFormationAlternatives [r | (_,Just r,_)<-rows]) value,changed) | (k,value,changed)<-rows]
          issued=[r | (_,Just r,True)<-finalRows]
          retained=M.fromList [(k,r) | (k,Just r,_)<-finalRows,not (materialScopeEnded material),
            u<candidateRevisionEnd (candidateBody r)]
      let lost=M.elems (M.difference (activeCandidates state) retained)++[r | (key,Just r,_)<-rows,M.notMember key retained]
          boundary=S.union (retiredParticipationObjects state) (S.fromList [groupTurnObject turn | r<-lost,(turn,_)<-candidateMembers (candidateBody r)])
      pure (Right (CandidateState retained boundary,issued))
  where
    material=pairMaterial view;u=materialProgress material;delta=groupDelta method
    affected=not (S.null (materialChanged material)) || materialScopeEnded material ||
      any (\row->let b=candidateBody row in
        candidateDomainIncomplete b/=materialCoverageIncomplete material ||
        (not (candidateClosed b) && u>=candidateDeadline b) || u>=candidateRevisionEnd b)
        (M.elems (activeCandidates state))
    -- 旧核心已过原r则本次不接纳修订。没有历史反查、补发或恢复。
    prior=M.filter (\r->u<=candidateRevisionEnd (candidateBody r) || not (candidateClosed (candidateBody r))) (activeCandidates state)
    canonical key=case [old | old<-M.keys prior,snd old==snd key] of
      [old]->old
      _->key
    prepare=do
      unless (finite delta && delta>0 && finite (groupObservationDuration method) && groupObservationDuration method>0) (Left "共同形成Δ非法")
      let wanted=S.toAscList (M.keysSet prior `S.union` S.fromList (map canonical (if S.null (materialChanged material) then [] else formationQuestions method view)))
      mapM_ (\(_,members)->unless (all (`M.member` materialTurns material) members)
        (Left "当前候选缺少其有限修正端点，不能读取latest替代")) wanted
      pure (prior,wanted)
    basis members=[p | (i,a)<-zip [0::Int ..] members,b<-drop (i+1) members,
      Just p<-[M.lookup (pairKey a b) (pairBases view)]]
    bodyFor key@(question,members) old
      | Just row <- old, u>candidateRevisionEnd (candidateBody row) =
          let b=candidateBody row in b {candidateClosed=True,
            candidateObservation=if candidateBasis b==Contradicted then Withdrawn
              else if candidateBasis b==Supported then ClosedSupported else ClosedInsufficient}
      | otherwise =
        let turns=[materialTurns material M.! k | k<-members]
            pairs=basis members
            decisions=map pairDecision pairs
            local | any groupTurnRetracted turns || PairVeto `elem` decisions=Contradicted
                  | length pairs==length members*(length members-1) `div` 2 && all (==PairPositive) decisions=Supported
                  | otherwise=Incomplete
            currentClocks=mapMaybe (fmap groupClockValue . groupTurnClock) turns
            anchor=if length currentClocks==length turns then minimum currentClocks else maybe (questionAnchor question) (candidateAnchor . candidateBody) old
            deadline=min (maybe (questionDeadline question) (candidateDeadline . candidateBody) old) (anchor+groupObservationDuration method)
            revisionEnd=min (maybe (questionRevisionEnd question) (candidateRevisionEnd . candidateBody) old) (deadline+6*delta)
            closed=maybe False (candidateClosed . candidateBody) old || u>=deadline
            observation | materialScopeEnded material=EndedByScope
                        | local==Contradicted=Withdrawn
                        | closed && local==Supported=ClosedSupported
                        | closed=ClosedInsufficient
                        | otherwise=Open
            memberStatus t=if all (\other->turnKey other==turnKey t ||
                  maybe False ((==PairPositive) . pairDecision) (M.lookup (pairKey (turnKey t) (turnKey other)) (pairBases view))) turns
              then ConfirmedMember else CandidateMember
        in CandidateBody [(t,memberStatus t) | t<-turns] pairs local Unambiguous observation
            (materialCoverageIncomplete material) anchor deadline revisionEnd closed [] []
    link lives allBodies key body=
      let sameProblem other=let b=allBodies M.! other in
            (candidateAnchor body,candidateDeadline body,candidateRevisionEnd body)==
            (candidateAnchor b,candidateDeadline b,candidateRevisionEnd b)
          members=S.fromList (snd key)
          covering=[lives M.! other | (other,b)<-M.toList allBodies,other/=key,sameProblem other,
            candidateBasis b==Supported,u<=candidateRevisionEnd b,members `S.isProperSubsetOf` S.fromList (snd other)]
          alternatives=[lives M.! other | (other,b)<-M.toList allBodies,other/=key,
            candidateBasis b/=Contradicted,candidateBasis body/=Contradicted,
            not (S.null (S.intersection members (S.fromList (snd other)))),
            not (sameProblem other && candidateBasis body==Supported && candidateBasis b==Supported &&
              (members `S.isSubsetOf` S.fromList (snd other) || S.fromList (snd other) `S.isSubsetOf` members))]
      in if u>candidateRevisionEnd body then body else body {candidateCoveredBy=sort covering,candidateOverlaps=sort alternatives,
        candidateAlternatives=if null alternatives then Unambiguous else UnresolvedOverlap,
        candidateObservation=if not (null covering) && candidateBasis body==Supported && not (materialScopeEnded material)
          then Subsumed else candidateObservation body}
    opaque=liftIO (UUID.toText <$> UUID.nextRandom)
