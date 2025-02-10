#!/usr/bin/env python

# 累加求和
from timeit import timeit

def task():
  N, total = 1000000, 0
  for x in range(N+1): total += x
  print(f'1+2+...+{N} = {total}')

runtime = timeit(
  stmt = 'task()',
  globals = globals(),
  number = 10
) / 10
print(f'算法耗时：{runtime} s')
