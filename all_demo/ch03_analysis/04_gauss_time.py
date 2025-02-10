#!/usr/bin/env python

from time import time
start = time()

# 高斯算法
N = 1000000
total = int((1+N)*N/2)
print(f'1+2+...+{N} = {total}')

end = time()
print(f'算法耗时：{end-start} s')
