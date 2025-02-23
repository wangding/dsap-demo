#!/usr/bin/env python

# 递归方式正序、逆序打印 n 个数
def print_n(n):
  if n<0: return
  print(n, end=' ')
  print_n(n-1)
  print(n, end=' ')

print_n(5)
