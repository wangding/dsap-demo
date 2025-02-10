#!/usr/bin/env python

# 查看内存消耗
# pip install psutil
import sys
import time
import psutil
import os

def get_memory_usage():
  process = psutil.Process(os.getpid())
  memory_info = process.memory_info()
  return memory_info.rss / (1024 ** 2)

data = []
for x in range(10):
  data.extend([i for i in range(100000)])
  memory_usage = get_memory_usage()
  print(f"数组元素数量: {len(data)}")
  print(f"数组内存占用：{sys.getsizeof(data)/ (1024 ** 2):.2f}  MB")
  print(f"进程内存占用: {memory_usage:.2f} MB\n")
  time.sleep(1)