#!/usr/bin/env python

from math import sqrt
from shape import Shape

# 等边三角形类，继承 Shape 类
class EqTriangle(Shape):
  def __init__(self, side): self.__side = side

  @property
  def side(self): return self.__side

  @property
  def perimeter(self): return 3 * self.__side

  @property
  def area(self): return sqrt(3) * self.__side ** 2 / 4
  def __mul__(self, scale): return EqTriangle(self.__side * scale)

if __name__ == '__main__':
  t = EqTriangle(1)
  print(f'triangle side:      {t.side}')
  print(f'triangle area:      {t.area:.2f}')
  print(f'triangle perimeter: {t.perimeter:.2f}\n')

  t = t * 2
  print(f'triangle side:      {t.side}')
  print(f'triangle area:      {t.area:.2f}')
  print(f'triangle perimeter: {t.perimeter:.2f}')
