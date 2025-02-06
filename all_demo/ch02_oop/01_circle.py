#!/usr/bin/env python

from math import pi

# 圆形类
class Circle:
  def __init__(self, radius): self.__radius = radius
  def perimeter(self): return 2 * pi * self.__radius
  def area(self): return pi * self.__radius ** 2

if __name__ == '__main__':
  radius = 1
  c = Circle(radius)
  print(f'circle radius:    {radius}')
  print(f'circle area:      {c.area():.2f}')
  print(f'circle perimeter: {c.perimeter():.2f}')
