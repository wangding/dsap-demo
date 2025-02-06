#!/usr/bin/env python

# 形状类
class Shape:
  @property
  def perimeter(self):
    raise NotImplementedError('must be implemented by subclass')

  @property
  def area(self):
    raise NotImplementedError('must be implemented by subclass')

  def __mul__(self, num):
    raise NotImplementedError('must be implemented by subclass')

if __name__ == '__main__':
  s = Shape()
  print(f'shape area:      {s.area}')
  print(f'shape object id: {id(s)}')
