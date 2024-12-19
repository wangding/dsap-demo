#!/usr/bin/env python

# 实验法验证 Python list 的扩容

import sys

data = []
for k in range(100):
  size = sys.getsizeof(data)
  print(f'Length: {len(data):3d};',
        f'Size in bytes: {size:4d}')
  data.append(None)
