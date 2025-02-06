#!/usr/bin/env python

from math import pi

# 圆形类，运算符重载实现缩放
class Circle:
  def __init__(self, radius): self.__radius = radius

  @property
  def radius(self): return self.__radius

  @property
  def perimeter(self): return 2 * pi * self.__radius

  @property
  def area(self): return pi * self.__radius ** 2
  def __mul__(self, num): self.__radius *= num; return self

if __name__ == '__main__':
  c = Circle(1)
  print(f'circle radius:    {c.radius}')
  print(f'circle area:      {c.area:.2f}')
  print(f'circle perimeter: {c.perimeter:.2f}\n')

  c = c * 2
  print(f'circle radius:    {c.radius}')
  print(f'circle area:      {c.area:.2f}')
  print(f'circle perimeter: {c.perimeter:.2f}')