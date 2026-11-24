# 当前锁定源码摘录

只读摘录；原始文件未修改。完整源码blob/SHA256见E01 implementation_sources。

## t0/gen/cc.py:131

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:t0/gen/cc.py`

```python
131:         "buy_price1": 买一价
132:         "buy_vol1": 买一量
133:         "sell_price1": 卖一价
134:         "sell_vol1": 卖一量
135:         "buy_order_price": 预测tick间的主买价(例如卖一盘口减少或者卖一盘口消失视为主买, 反之, 卖一盘口量增加或者价格反向移动则主买量价均视为0,以下卖方同理)
136:         "buy_order_vol": 预测tick间的主买量
137:         "sell_order_price": 预测tick间的主卖价
138:         "sell_order_vol": 预测tick间的主卖量
139: 
140:     """
141: 
142:     params = lambda: {
143:     }
144: 
145:     def _impl(self):
146:         import re
147:         sym = re.sub(r'\d+',"",self.sym)  # 去掉合约名中的数字得到品种名
148:         calendar_name = CurrCalendar.name(True)
149:         cn = sym if calendar_name == "@" else calendar_name
150:         cc_dir = f"{self.sof.ori_dir}/sub_continuous_contract/dba/{sym}_{cn}"
151:         cal_dir = f"{self.sof.ori_dir}/calendar/{cn}"
152: 
153:         trade_volume = DbArray(cc_dir, "trade_volume")
154:         open_interest = DbArray(cc_dir, "open_interest")
155:         price = DbArray(cc_dir, "price")
156:         tsa = DbArray(cal_dir, "natural_tsa", "M8[ns]")
157:         linear_tsa = DbArray(cal_dir, "linear_tsa", "i8")
158: 
159:         # -------------------------
160:         buy_price1 = DbArray(cc_dir, "buy_price1")
161:         buy_vol1 = DbArray(cc_dir, "buy_vol1")
162:         sell_price1 = DbArray(cc_dir, "sell_price1")
163:         sell_vol1 = DbArray(cc_dir, "sell_vol1")
164:         buy_order_price = DbArray(cc_dir, "buy_order_price")
165:         buy_order_vol = DbArray(cc_dir, "buy_order_vol")
166:         sell_order_price = DbArray(cc_dir, "sell_order_price")
167:         sell_order_vol = DbArray(cc_dir, "sell_order_vol")
168: 
169:         df = pd.DataFrame(
170:             data={
171:                 "trade_volume": trade_volume.ndarray[:],
172:                 "open_interest": open_interest.ndarray[:],
173:                 "price": price.ndarray[:],
174:                 "linear_ts": linear_tsa.ndarray[:],
175:                 "buy_price1": buy_price1.ndarray[:],
176:                 "buy_vol1": buy_vol1.ndarray[:],
177:                 "sell_price1": sell_price1.ndarray[:],
178:                 "sell_vol1": sell_vol1.ndarray[:],
179:                 "buy_order_price": buy_order_price.ndarray[:],
180:                 "buy_order_vol": buy_order_vol.ndarray[:],
181:                 "sell_order_price": sell_order_price.ndarray[:],
182:                 "sell_order_vol": sell_order_vol.ndarray[:],
183:             },
184:             index=tsa.ndarray[:],
```

## hf/mc.py:19

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/mc.py`

```python
19:     if sof is None:
20:         sof = CurrTradeSet.sof(True)
21:     main_df = pd.read_csv(
22:         f"{sof.sof_dir}/tlist/main_contract/{sym}.csv",
23:         parse_dates=["date"],
24:     )
25:     for c in ["start_ts", "end_ts"]:
26:         main_df[c] = pd.to_datetime(main_df[c])
27:     for _, r in main_df.iterrows():
28:         yield r.date, r.max_sym_ct, slice(r.start_ts, r.end_ts)
29: 
30: 
31: def main_tick_data(startDay, endDay, sym=None, sof=None, cale=None, extraTime=0):
32:     if sym is None:
33:         sym = CurrSymbol.sym(True)
34:     if sof is None:
35:         sof = CurrTradeSet.sof(True)
```

## hf/prel0/tick_quote_context.py:160

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/tick_quote_context.py`

```python
160:     def _load_cc_df(self):
161:         """读取并限定到当前 Sof 日期范围的连续主力一档盘口基础数据。"""
162:         if SubContinuousContract is None:
163:             raise ImportError("项目运行环境不可用，无法读取 SubContinuousContract")
164:         cc_df = SubContinuousContract().rerun().F.value
165:         sof = CurrTradeSet.sof(True)
166:         return cc_df[sof.startDay : sof.endDay]
```

## hf/prel0/tick_quote_context.py:220

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/tick_quote_context.py`

```python
220:     def _trading_day_chunk_plan(self, cc_df):
221:         """只保留轻量行区间；不提前创建并常驻所有交易日 DataFrame。"""
222:         index = cc_df.index
223:         plan = []
224:         chunk_id = 0
225:         for trade_day, _contract, duration in trading_days():
226:             start = int(index.searchsorted(pd.Timestamp(duration.start), side="left"))
227:             stop = int(index.searchsorted(pd.Timestamp(duration.stop), side="right"))
228:             if stop <= start:
229:                 continue
230:             plan.append((chunk_id, pd.Timestamp(trade_day), start, stop))
231:             chunk_id += 1
232:         if cc_df.shape[0] > 0:
233:             if not plan:
234:                 raise ValueError("交易日区间没有覆盖 SubContinuousContract 输入")
235:             expected_start = 0
236:             for _chunk_id, trade_day, start, stop in plan:
237:                 if start != expected_start:
238:                     raise ValueError(
239:                         f"交易日区间在 {trade_day} 前不连续: {expected_start} != {start}"
240:                     )
241:                 expected_start = stop
242:             if expected_start != int(cc_df.shape[0]):
243:                 raise ValueError(
244:                     f"交易日区间未覆盖完整输入: {expected_start} != {cc_df.shape[0]}"
245:                 )
246:         return plan
```

## hf/prel0/pressure_big_deal.py:225

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/pressure_big_deal.py`

```python
225: ):
226:     """内部共享 helper：按交易日分块执行 F3/F4 子路径。"""
227:     support = PressureBigDealWrapperSupport()
228:     if lane_thresholds_map is not None and lane_threshold_source is not None:
229:         raise ValueError("lane_thresholds_map/source 只能提供一个")
230:     chunk_plan = support._trading_day_chunk_plan(cc_df)
231:     total_chunks = len(chunk_plan)
232:     total_ticks = int(sum(stop - start for _chunk_id, _trade_day, start, stop in chunk_plan))
233:     support._log_chunk_plan(logger, sym, feature_name, total_chunks)
234: 
235:     for done_chunks, (chunk_id, trade_day, chunk_df) in enumerate(
236:         support._iter_trading_day_chunks(cc_df, chunk_plan), start=1
237:     ):
238:         compute_started = time.perf_counter()
239:         tape = support._build_pressure_big_deal_tape(chunk_df)
240:         arrays = normalize_pressure_big_deal_inputs(tape)
241:         chunk_meta = support._chunk_meta(
242:             chunk_id=chunk_id,
243:             boundary_type="trading_day",
244:             chunk_df=chunk_df,
245:             trade_day=trade_day,
246:         )
247:         if lane_threshold_source is not None:
248:             aligned_thresholds = support._align_lane_threshold_source(
249:                 chunk_df.index, lane_threshold_source
250:             )
251:         elif lane_thresholds_map:
252:             start_pos = int(cc_df.index.searchsorted(chunk_df.index[0], side="left"))
253:             stop_pos = int(cc_df.index.searchsorted(chunk_df.index[-1], side="right"))
254:             aligned_thresholds = _slice_lane_thresholds_map(
255:                 lane_thresholds_map=lane_thresholds_map,
256:                 start_pos=start_pos,
257:                 stop_pos=stop_pos,
258:             )
259:         else:
260:             aligned_thresholds = {}
261:         chunk_out = compute_pressure_big_deal_chunk(
262:             trade_vol=arrays["trade_vol"],
263:             buy_hit_px=arrays["buy_hit_px"],
```

## hf/prel0/pressure_big_deal.py:579

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/pressure_big_deal.py`

```python
579:     params = lambda: dict(
580:         parameter_set_id="tactical-default",
581:         qualification_family="tactical",
582:         amt_n=30,
583:         lane_threshold_map=FAnyParam(
584:             {"tactical": ["0.99", "0.995"]}
585:         ),
586:         same_best_tol_ticks=0,
587:         big_deal_ratio_min=1.0,
588:     )
589: 
590:     def _impl(self):
591:         sym = CurrSymbol.sym()
592: 
593:         families = tuple(self.P.lane_threshold_map.keys())
594:         if families != (self.P.qualification_family,):
595:             raise ValueError(
596:                 "DirectedBigDealTick 每个 Feature 实例必须且只能绑定一个 qualification_family"
597:             )
598: 
599:         cc_df = self._load_cc_df()
600:         trading_unit = self._load_trading_unit()
601:         tick_size = self._load_tick_size(cc_df)
602:         threshold_source = self._load_lane_threshold_source()
603:         availability_key = "directed_large_deal_availability_dense"
604:         availability_schema = _large_deal_availability_schema()
605:         params = {
606:             "qualification_family": self.P.qualification_family,
607:             "lane_threshold_map": dict(self.P.lane_threshold_map.items()),
608:             "same_best_tol_ticks": self.P.same_best_tol_ticks,
609:             "big_deal_ratio_min": self.P.big_deal_ratio_min,
610:             "trading_unit": trading_unit,
611:         }
612: 
613:         def execute(append_chunk):
614:             compact_results = []
615:             for chunk in _iter_pressure_big_deal_trading_day_chunks(
616:                 cc_df=cc_df,
617:                 tick_size=tick_size,
618:                 trading_unit=trading_unit,
619:                 lane_thresholds_map=None,
620:                 lane_threshold_source=threshold_source,
621:                 same_best_tol_ticks=self.P.same_best_tol_ticks,
622:                 big_deal_ratio_min=self.P.big_deal_ratio_min,
623:                 eps_vol=DEFAULT_EPS_VOL,
624:                 compute_f3=False,
625:                 compute_f4=True,
```

## hf/prel0/wall_assembler.py:432

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/wall_assembler.py`

```python
432: def _exclude_empty_calendar_padding(cc_df, trading_day_ranges, logger=None):
433:     """因果地排除时段首条全空占位，保留原时间坐标和所有有效报价。
434: 
435:     排除决定只依赖当前报价和此前时间间隔，不等待或查看下一拍。
436:     连续空行和时段内部全空行不属于此规则，继续拒绝消费。
437:     """
438:     index = cc_df.index
439:     if len(index) == 0:
440:         return cc_df
441:     quote_columns = ["price", "buy_price1", "buy_vol1", "sell_price1", "sell_vol1"]
442:     half_second = pd.Timedelta(milliseconds=500)
443:     segment_start = np.r_[True, np.diff(index.asi8) > half_second.value]
444:     empty = np.ones(len(index), dtype=bool)
445:     for column in quote_columns:
446:         empty &= cc_df[column].isna().to_numpy()
447:     unexpected_empty = np.flatnonzero(empty & ~segment_start)
448:     if unexpected_empty.size:
449:         stamp = index[unexpected_empty[0]]
450:         raise ValueError(f"时段内部或连续全空行情不能作为开盘占位排除: {stamp}")
451:     excluded = np.flatnonzero(segment_start & empty)
452:     covered = np.zeros(len(cc_df), dtype=bool)
453:     for duration in trading_day_ranges:
454:         start = int(index.searchsorted(pd.Timestamp(duration.start), side="left"))
455:         stop = int(index.searchsorted(pd.Timestamp(duration.stop), side="right"))
456:         covered[start:stop] = True
457:     covered[excluded] = True
458:     if not covered.all():
459:         raise ValueError("交易日区间外存在有效行情或非半秒开盘占位，拒绝丢弃输入")
460:     if excluded.size == 0:
461:         return cc_df
462:     keep = np.ones(len(cc_df), dtype=bool)
463:     keep[excluded] = False
464:     # 仅复制本 Feature 消费的列；原始 DBA、空占位及其时间轴保持原样。
465:     selected = cc_df.loc[keep, quote_columns + ["linear_ts"]].copy()
466:     timestamps = [stamp.isoformat() for stamp in index[excluded]]
467:     selected.attrs.update(cc_df.attrs)
468:     cut = source_scope(CurrSymbol.sym(), cc_df, calendar=CurrCalendar.name(True))["market_source_cut"]
469:     selected.attrs["market_source_cut"] = cut + "|excluded-empty-calendar-padding:" + ",".join(timestamps)
470:     if logger is not None:
471:         logger.warning("Wall 输入排除全空半秒日历占位 %d 行: %s", len(timestamps), timestamps)
```

## hf/prel0/wall_assembler.py:756

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/wall_assembler.py`

```python
756:     def _load_cc_df(self):
757:         cc_df = super()._load_cc_df()
758:         ranges = tuple(duration for _day, _contract, duration in trading_days())
759:         return _exclude_empty_calendar_padding(cc_df, ranges, logger=self.logger)
```

## hf/prel0/attack_flow_assembler.py:535

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/attack_flow_assembler.py`

```python
535:     results = []
536:     carry_state = {"bid": None, "ask": None}
537:     compact_formation_carry = {"bid": None, "ask": None}
538:     capability_formation_carry = {"bid": None, "ask": None}
539:     qualification_hit_book = {"bid": {}, "ask": {}}
540:     next_segment_id = 1
541:     chunk_plan = support._trading_day_chunk_plan(cc_df)
542:     total_chunks = len(chunk_plan)
543:     support._log_chunk_plan(logger, sym, feature_name, total_chunks)
544:     wall_columns = [
545:         f"wall_{field}_{side}"
546:         for side in ("bid", "ask")
547:         for field in ("id", "side_code", "status_code", "band_lo", "band_hi", "core_price")
548:     ]
549:     f4_columns = [
550:         "uti", "side_code", "qualification_family_code", "grade",
551:         "deal_amt", "directional_hit_volume_proxy", "qualification_code",
552:     ]
553:     missing_f4 = sorted(set(f4_columns) - set(directed_large_deal_df.columns))
554:     if missing_f4 and directed_large_deal_df.shape[0] > 0:
555:         raise ValueError(f"F4 artifact 缺字段: {missing_f4}")
556: 
557:     for done, (chunk_id, trade_day, chunk_df) in enumerate(
558:         support._iter_trading_day_chunks(cc_df, chunk_plan), start=1
559:     ):
560:         meta = support._chunk_meta(chunk_id=chunk_id, boundary_type="trading_day", chunk_df=chunk_df, trade_day=trade_day)
561:         wall = _require_exact_axis("Wall artifact", wall_state_trace_df, chunk_df.index, wall_columns)
562:         uti = _uti_from_linear_ts(chunk_df.linear_ts.values)
563:         f4_sparse = select_sorted_uti_range(
564:             "F4 artifact", directed_large_deal_df, uti
565:         )
566:         wall_events = select_sorted_uti_range(
567:             "Wall event artifact", wall_events_df, uti
568:         )
569:         availability = _require_exact_axis(
570:             "F4 availability artifact", directed_large_deal_availability_df, chunk_df.index,
571:             ["availability_code", "activity_code"],
572:         )
```

## hf/prel0/attack_flow_assembler.py:755

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/attack_flow_assembler.py`

```python
755:     def _impl(self):
756:         sym = CurrSymbol.sym()
757:         cc_df = self._load_cc_df()
758:         wall_result = self.P.wall.run().F
759:         wall_receipt = load_p1_product_receipt(self.P.wall, "wall_lifecycle")
760:         validate_product_artifact(
761:             wall_receipt,
762:             {key: value for key, value in wall_result.items() if key.startswith("wall__")},
763:         )
764:         selected_features = (
765:             self.P.directed_large_deal_tactical,
766:             self.P.directed_large_deal_structural,
767:         ) + tuple(self.P.additional_directed_large_deal_features)
768:         f4_receipts = []
769:         f4_parts = []
770:         availability_frames = []
771:         for stream_ordinal, selected_feature in enumerate(selected_features):
772:             result = selected_feature.run().F
773:             receipt = load_p1_product_receipt(
774:                 selected_feature, "directed_large_deal_stream"
775:             )
776:             streams = {
777:                 key: value
778:                 for key, value in result.items()
779:                 if key.startswith("buy") or key.startswith("sell")
780:             }
781:             validate_product_artifact(receipt, streams)
782:             family = receipt["actual_business_parameters"]["qualification_family"]
783:             family_code = {"tactical": 1, "structural": 2}.get(family, 3)
784:             for value in streams.values():
785:                 frame = value.copy()
786:                 frame["selected_stream_ordinal"] = np.int64(stream_ordinal)
787:                 frame["qualification_family_code"] = np.int8(family_code)
788:                 f4_parts.append(frame)
789:             availability_frames.append(result.directed_large_deal_availability_dense)
790:             f4_receipts.append(receipt)
791:         if not f4_receipts:
792:             raise ValueError("AttackFlowAssembler 至少需要一个显式选择的 F4 Feature")
793:         f4_flat = pd.concat(f4_parts, axis=0).sort_index() if f4_parts else pd.DataFrame()
794:         availability = availability_frames[0]
795:         first_scope = f4_receipts[0]["source_scope"]
796:         if any(receipt["source_scope"] != first_scope for receipt in f4_receipts[1:]):
797:             raise ValueError("所选 F4 Feature 的 source scope 不一致")
798:         results = run_attack_flow_assembler_trading_day_chunks(
```

## hf/prel0/p1_dba_export.py:540

来源：`daowei2026/tis@179016111ed0394f92025313e46bd13534932a74:hf/prel0/p1_dba_export.py`

```python
540:         if not pending:
541:             raise P1ReceiptError("P1 Feature 未形成产品 receipt，拒绝提交 artifact")
542:         plans = [value for value in res.values() if isinstance(value, P1ChunkedArtifactPlan)]
543:         if plans:
544:             if len(plans) != 1 or len(res) != 1:
545:                 raise P1ReceiptError("chunked result 必须只含一个执行计划")
546:             plan = plans[0]
547:             writer = _P1ChunkedDbaWriter(
548:                 (full_dir, *tuple(self.backup_full_dirs)),
549:                 plan.specs,
550:             )
551:             started = time.perf_counter()
552:             ordinary_frames = plan.execute(writer.append)
553:             execute_seconds = time.perf_counter() - started
554:             started = time.perf_counter()
555:             writer.finalize(ordinary_frames)
556:             finalize_seconds = time.perf_counter() - started
557:             self.logger.info(
```
