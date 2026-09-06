# nbphy
python基础物理库，可以做一些基础的物理计算

## 快速开始
```python
import nbphy
F = nbphy.force(100, "N") #力100N
s = nbphy.displacement(5, "m") #距离5m
W = F*s #500
print(W)
```

## 模块介绍
### `core`核心模块
- `displacement`距离 `force`力 `work`功
- `time`时间 `lever`杠杆 `velocity`速度
- `density`密度 `pressure`压强 `tabular`表格绘制函数
- `heat`热量 `specific_heat_capacity`比热容
### `nbphy.const`常量模块
- `g`重力加速度 `c`光速
- `pi`圆周率 `density_of_water`水的密度
- `specific_heat_capacity_of_water`水的比热容

## 示例代码
```python
import nbphy
field = ["钩码质量(g)", "弹簧测力计示数(N)"]
row = [
    [50, 0.5],
    [100, 1],
    [150, 1.5],
    [200, 2]
]
print(nbphy.tabular(field, row))
data = [3.40, 3.45, 3.47]
print(nbphy.average(data))
```

## 许可证
MIT
