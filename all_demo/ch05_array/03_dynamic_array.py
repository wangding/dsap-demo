#!/usr/bin/env python

# 用 ctypes 模块实现动态数组
from ctypes import py_object
class DynamicArray:
  def __init__(self):
    self.__A = (py_object*1)()
    self.__n = 0
    self.__capacity = 1

  def __len__(self): return self.__n
  def __getitem__(self, k):
    if self.__n == 0: raise Exception('数组为空')
    if not 0<= k < self.__n: raise Exception('数组下标越界')
    return self.__A[k]
  
  def __setitem__(self, k, obj):
    if not 0<= k <= self.__n: raise Exception('数组下标越界')
    self.__A[k] = obj

  def __str__(self):
    return '[%s]' % (', '.join([str(self.__A[i]) for i in range(self.__n)]))
  
  # def __iter__(self):
  #   for i in range(self.__n): yield self.__A[i]

  def append(self, obj):
    if self.__n == self.__capacity: self.__resize(2*self.__capacity)
    self[self.__n] = obj
    self.__n += 1

  def __resize(self, n):
    B = (py_object*n)()
    for i in range(self.__n): B[i] = self[i]
    self.__A = B
    self.__capacity = n

if __name__ == '__main__':
  arr = DynamicArray()
  arr.append(1)
  print(len(arr))
  print(arr)

  arr.append(2)
  print(len(arr))
  print(arr)

  arr.append(3)
  print(len(arr))
  print(arr)
  # for x in arr: print(x)