#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

# 形状抽象基类
class Shape(metaclass=ABCMeta):
  @property
  @abstractmethod
  def perimeter(self): pass

  @property
  @abstractmethod
  def area(self): pass

  @abstractmethod
  def __mul__(self, num): pass

if __name__ == '__main__':
  s = Shape()
  print(f'shape area:      {s.area}')
  print(f'shape object id: {id(s)}')
