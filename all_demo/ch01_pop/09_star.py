#!/usr/bin/env python

# 画五角星
from turtle import *

def init():
  color('blue')
  width(3)
  shape('turtle')

def star(side_length=400):
  for i in range(5):
    forward(side_length)
    right(144)

def main():
  init()
  star()
  mainloop()

main()
