#!/usr/bin/env python

# 转着圈画方形
from turtle import *

def init():
  color('blue')
  speed(0)
  shape('turtle')

def square():
  for i in range(4):
    forward(200)
    right(90)

def main():
  init()
  for i in range(60):
    square()
    right(6)
  mainloop()

main()
