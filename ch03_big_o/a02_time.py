#!/usr/bin/env python

# 实验法测量算法运行时长
# 用 time 模块的 process_time 方法

from time import process_time

def task():
  num = []
  for i in range(10**5):
    num.append(i)
  num.reverse()

start = process_time()
task()
end = process_time()
print(f'Execution time: {end-start:.3f} s')
