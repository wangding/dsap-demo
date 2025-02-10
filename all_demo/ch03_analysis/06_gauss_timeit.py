#!/usr/bin/env python

from timeit import timeit

# 高斯算法
def task():
  N = 1000000
  total = int((1+N)*N/2)
  print(f'1+2+...+{N} = {total}')

runtime = timeit(
  stmt = 'task()',
  globals = globals(),
  number = 10
) / 10
print(f'算法耗时：{runtime} s')
