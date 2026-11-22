# D013合同校验范围

`validate_s1.py --draft`在冻结前检查原S1合同与同次实际材料；原生预期于校验后冻结；`validate_s1.py`再核正式文件及FREEZE_MANIFEST。未执行原S2正式证据对照或新增专业Gate。

全部准确材料由锁定Git对象读取，21份gzip/JSON身份一致。CaseMaterialIndex的原行、UUID完整位/父坐标、独立上游actual/几何confirm/selected-known/point-known及边界内外精确匹配。浏览器收据和截图身份均核对，原HTML未改变。原四问题与七索引没有回写。

发布时再核全部专业文件manifest及本次写面。原V2 schema/gate不改；该锁定版完整validate-executor-return的binding()硬编码ChatGPT manager，与本Run既有Codex manager不兼容，故只真实调用其validated、pro_state、object_ref_fields并校验实际I/D/Binding/授权/已发布结果。不得把这项部分函数校验表述成完整CLI通过，也不伪造独立controller回执。
