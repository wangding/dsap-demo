#!/usr/bin/env python

# 绘制分形树
from turtle import *

def tree(length):
  if length < 10: return
  # main branch
  forward(length)
  # left branch
  left(ANGLE)
  tree(length*0.7)
  # right branch
  right(ANGLE*2)
  tree(length*0.7)
  # back home
  left(ANGLE)
  backward(length)

ANGLE = 30
speed(100)
left(90)
tree(100)
mainloop()
