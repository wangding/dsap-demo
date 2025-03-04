#!/usr/bin/env python

# 紧凑数组
from array import array
from sys import getsizeof

for n in range(1, 5):
  arr = array('i', range(10**n))
  lst = list(range(10**n))
  print(f'{10**n} 个数组元素:')
  print(f'紧凑数组大小: {getsizeof(arr)} 字节')
  print(f'引用数组大小: {getsizeof(lst)} 字节\n')
