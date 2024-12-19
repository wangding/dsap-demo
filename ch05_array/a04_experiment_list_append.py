#!/usr/bin/env python

# 实验法测试 Python list 类 append 效率

from time import time

def compute_average(n):
  data = []
  start = time()
  for k in range(n):
    data.append(None)
  end = time()
  return (end - start) / n

n, maxN = 10, 10000000
while n <= maxN:
  cost = compute_average(n) * 1000000 # 单位微秒
  print(f'Average of {cost:.3f} for n={n}')
  n *= 10
