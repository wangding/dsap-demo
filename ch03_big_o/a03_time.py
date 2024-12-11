#!/usr/bin/env python

# 实验法测量算法运行时长
# 用 timeit 模块的 timeit 方法

from timeit import timeit

def task():
  num = []
  for i in range(10**5):
    num.append(i)
  num.reverse()

t = timeit(
      stmt = 'task()',
      globals = globals(),
      number = 5
    )

print(f'Execution time: {t/5:.3f} s')
