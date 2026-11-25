# pairwise-icc-profile-transform

## 领域

游戏、图形与多媒体

## 主题

ICC 配置文件转换

## 说明

LUT 转换、黑点补偿与逐图读配置。

初始状态下 `imaging/icc_profile_transform.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
