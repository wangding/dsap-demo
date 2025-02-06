#!/usr/bin/env python

from math import pi
from shape import Shape

# 圆形类，继承 Shape 类
class Circle(Shape):
  def __init__(self, radius): self.__radius = radius

  @property
  def radius(self): return self.__radius

  @property
  def perimeter(self): return 2 * pi * self.__radius

  @property
  def area(self): return pi * self.__radius ** 2
  def __mul__(self, scale): return Circle(self.__radius * scale)

if __name__ == '__main__':
  c = Circle(1)
  print(f'circle radius:    {c.radius}')
  print(f'circle area:      {c.area:.2f}')
  print(f'circle perimeter: {c.perimeter:.2f}\n')

  c = c * 2
  print(f'circle radius:    {c.radius}')
  print(f'circle area:      {c.area:.2f}')
  print(f'circle perimeter: {c.perimeter:.2f}')
