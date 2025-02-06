#!/usr/bin/env python

from shape import Shape

# 正方形类，继承 Shape 类
class Square(Shape):
  def __init__(self, side): self.__side = side

  @property
  def side(self): return self.__side

  @property
  def perimeter(self): return 4 * self.__side

  @property
  def area(self): return self.__side ** 2
  def __mul__(self, scale): return Square(self.__side * scale)

if __name__ == '__main__':
  s = Square(1)
  print(f'square side:      {s.side}')
  print(f'square area:      {s.area:.2f}')
  print(f'square perimeter: {s.perimeter:.2f}\n')

  s = s * 2
  print(f'square side:      {s.side}')
  print(f'square area:      {s.area:.2f}')
  print(f'square perimeter: {s.perimeter:.2f}')
