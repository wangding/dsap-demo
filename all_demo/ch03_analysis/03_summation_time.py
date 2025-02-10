#!/usr/bin/env python

# 累加求和
from time import time

start = time()

N, total = 1000000, 0
for x in range(N+1): total += x
print(f'1+2+...+{N} = {total}')

end = time()
print(f'算法耗时：{end-start} s')
