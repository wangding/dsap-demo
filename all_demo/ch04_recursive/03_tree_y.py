#!/usr/bin/env python

# 绘制分形树的一个树杈 Y
from turtle import *

def y(length):
  # main branch
  forward(length)
  # left branch
  left(ANGLE)
  forward(length*0.7)
  backward(length*0.7)
  # right branch
  right(ANGLE*2)
  forward(length*0.7)
  backward(length*0.7)
  # back home
  left(ANGLE)
  backward(length)

ANGLE = 30
speed(100)
left(90)
y(100)
mainloop()
