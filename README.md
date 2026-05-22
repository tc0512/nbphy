# nbphy
python零依赖物理库，可以做一些基础的物理计算

## 快速开始
```python
import nbphy
F = nbphy.force(100, "N") #力100N
s = displacement(5, "m") #距离5m
W = F*s #500
print(W)
```

## 模块介绍
### `core`核心模块
- `displacement`距离 `force`力 `work`功
- `time`时间 `lever`杠杆 `velocity`速度
- `density`密度 `pressure`压强 `tabular`表格绘制函数
### `nbphy.const`常量模块
- `g`重力加速度 `c`光速
- `pi`圆周率 `density_of_water`水的密度

## 示例代码
