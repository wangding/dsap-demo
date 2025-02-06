#!/usr/bin/env python

# 画三个尺寸方形，方形函数带默认参数
from turtle import *

def init():
  color('blue')
  width(3)
  shape('turtle')

def square(side_length=100):
  for i in range(4):
    forward(side_length)
    right(90)

def main():
  init()
  square(50)
  square()
  square(150)
  mainloop()

main()
