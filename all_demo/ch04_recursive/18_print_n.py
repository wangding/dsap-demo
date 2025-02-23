#!/usr/bin/env python

# 循环方式正序、逆序打印 n 个数
def print_n(n):
  for x in range(n, -1, -1): print(x, end=' ')
  for x in range(n+1): print(x, end=' ')

print_n(5)
