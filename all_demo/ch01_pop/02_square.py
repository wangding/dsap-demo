#!/usr/bin/env python

# 画一个方形
# 使用循环语句，避免重复代码
from turtle import *

color('blue')
width(3)
shape('turtle')

for i in range(4):
  forward(200)
  right(90)

mainloop()
