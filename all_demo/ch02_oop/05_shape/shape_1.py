#!/usr/bin/env python

# 形状类
class Shape:
  @property
  def perimeter(self): pass

  @property
  def area(self): pass
  def __mul__(self, num): pass

if __name__ == '__main__':
  s = Shape()
  print(f'shape area:      {s.area}')
  print(f'shape object id: {id(s)}')
