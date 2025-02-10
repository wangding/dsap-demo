#!/usr/bin/env python

# N 个连续整数
from timeit import timeit

def task():
  N = 100000
  L = [x for x in range(N-1, -1, -1)]
  print(f'L = [{L[0]}, {L[1]}, ..., {L[N-1]}]')

runtime = timeit(
  stmt = 'task()',
  globals = globals(),
  number = 10
) / 10
print(f'算法耗时：{runtime} s')
