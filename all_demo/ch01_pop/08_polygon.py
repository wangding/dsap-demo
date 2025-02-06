#!/usr/bin/env python

# 画等边多边形，多边形函数带默认参数
from turtle import *

def init():
  color('blue')
  width(3)
  shape('turtle')

def polygon(sides=4, side_length=100):
  angle = 360/sides
  for i in range(sides):
    forward(side_length)
    right(angle)

def main():
  init()
  polygon(6, 250)
  polygon(5, 200)
  polygon(4, 150)
  polygon(3, 100)
  mainloop()

main()
