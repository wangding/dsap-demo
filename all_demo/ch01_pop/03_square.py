#!/usr/bin/env python

# 画一个方形
# 定义画方形的函数
from turtle import *

def init():
  color('blue')
  width(3)
  shape('turtle')

def square():
  for i in range(4):
    forward(200)
    right(90)

def main():
  init()
  square()
  mainloop()

main()
