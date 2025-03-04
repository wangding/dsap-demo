#!/usr/bin/env python

# 用 ctypes 模块实现静态数组
from ctypes import py_object
class StaticArray:
  def __init__(self, n):
    self.__A = (py_object*n)()
    self.__capacity = n

  def __len__(self):             return self.__capacity
  def __getitem__(self, k):      return self.__A[k]
  def __setitem__(self, k, obj): self.__A[k] = obj
  def __repr__(self):
    return '[%s]' % (', '.join([str(self.__A[i]) for i in range(self.__capacity)]))

if __name__ == '__main__':
  arr = StaticArray(5)
  print(len(arr))
  for i in range(5): arr[i] = i
  print(arr)
  arr[0] = 'hello'
  print(arr)