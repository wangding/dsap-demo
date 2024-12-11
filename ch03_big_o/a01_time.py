#!/usr/bin/env python

# 实验法测量算法运行时长
# 用 time 模块的 time 方法

from time import time

def task():
  num = []
  for i in range(10**5):
    num.append(i)
  num.reverse()

start = time()
task()
end = time()
print(f'Execution time: {end-start:.3f} s')
