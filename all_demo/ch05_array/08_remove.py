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

  def __repr__(self):
    return '[%s]' % (', '.join([str(self.__A[i]) for i in range(self.__n)]))
  
  def append(self, obj):
    if self.__n == self.__capacity: self.__resize(2*self.__capacity)
    self[self.__n] = obj
    self.__n += 1

  def insert(self, k, value):
    if self.__n == self.__capacity: self.__resize(2 * self._capacity)
    for j in range(self.__n, k, -1): self.__A[j] = self.__A[j-1]
    self.__A[k] = value
    self.__n += 1

  def sort(self):
    for x in range(1, self.__n):
      num = self.__A[x]
      while x>0:
        if self.__A[x-1] > self.__A[x]:
          self.__A[x] = self.__A[x-1]
          self.__A[x-1] = num
          x -= 1
        else: break

  def remove(self, e):
    if self.__n == 0: raise Exception('数组为空')
    for i in range(self.__n):
      if self.__A[i] == e:
        for j in range(i, self.__n-1): self.__A[j] = self.__A[j+1]
        self.__n -= 1
        return
    raise Exception(f'列表中没有 {e}')

  def __resize(self, n):
    B = (py_object*n)()
    for i in range(self.__n): B[i] = self[i]
    self.__A = B
    self.__capacity = n

if __name__ == '__main__':
  arr = DynamicArray()
  for x in range(1, 6): arr.append(x)
  print('befor delete:', arr)
  print('after delete:', end=' ')
  # arr.remove(1)
  # print(arr)
  # arr.remove(3)
  # print(arr)
  # arr.remove(5)
  # print(arr)
  # arr.remove(8)   # 删除不存在的元素
  # print(arr)
