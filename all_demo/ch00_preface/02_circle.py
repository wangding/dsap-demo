#!/usr/bin/env python

from math import pi

radius = float(input('请输入圆的半径：'))
perimeter = 2 * pi * radius
area = pi * radius ** 2

print(f"圆的面积为：{area:.2f}")
print(f"圆的周长为：{perimeter:.2f}")
