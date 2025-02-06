#!/usr/bin/env python

# 旋转着画正方形，每次旋转正方形的尺寸会变大
from turtle import *

def init():
  color('blue')
  speed(0)
  shape('turtle')

def square(side_length=100):
  for i in range(4):
    forward(side_length)
    right(90)

def main():
  init()
  side_length = 50
  for x in range(60):
    square(side_length)
    side_length += 5
    right(5)
  mainloop()

main()
