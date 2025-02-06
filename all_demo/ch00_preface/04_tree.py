#!/usr/bin/env python

from turtle import *

def tree(length):
  if length < 10: return
  forward(length)
  left(ANGLE)
  tree(length*0.7)
  right(ANGLE*2)
  tree(length*0.7)
  left(ANGLE)
  backward(length)

ANGLE = 30
speed(100)
left(90)
tree(100)
mainloop()
