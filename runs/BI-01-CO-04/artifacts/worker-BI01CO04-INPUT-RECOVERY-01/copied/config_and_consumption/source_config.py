"""Verified GTQH L1 dataset. Added source only; does not replace any default."""
import os as __os__
base_dir = ('F:' if __os__.name == 'nt' else '/m3varF') + '/BaseData/futures/GTQH_L1_20210104_20240208'
sof_name = 'GTQH_L1_20210104_20240208'
sof_label = 'GTQH L1 index m/rb/hc/i 20210104-20240208'
sof_category = 'BaseData/futures'
sof_dir = base_dir + '/sof'
ori_dir = base_dir + '/tick'
pnv_dir = base_dir + '/pnv'
sof_tlist_dir = base_dir + '/sof/tlist'
sof_unit_dir = base_dir + '/sof/unit/attribute'
calendar_dir = base_dir + '/sof'
stk_tlist = 'gtqh_four'
calendar_name = '@'
freqs = ('5s', '1m', '5m', '15m', '30m', '60m', '240m', '1d', '1W', '1M')
synthectic_syms = []
contract_names = []
block_fixed = {'steel': ['rb', 'hc', 'i'], 'oil_fat': ['m']}
block_ask = {'default': {'steel': ['rb', 'hc', 'i'], 'oil_fat': ['m']}}

# 工作区日历别名：钢铁三品种行情的开收盘 UTI/时间已逐行核对一致。
# 仅在测试目录链接 F 盘原日历；不修改正式数据目录。
sof_dir = '/dwdhome/fy/BASE_E6_2/mquant/aidata/test_runs/fy_owner_1d_30m_20261027/storage_migration_20261101/source_metadata/sof'
