#!/usr/bin/env python

# 递归打印九九乘法表
def table(n):
  if n == 0: return
  table(n-1)
  for m in range(1, n+1): print(f'{m}×{n}={m*n}', end=' ')
  print()

num = int(input('Please input num[1-9]: '))
if not 1<= num <= 9: raise Exception('num 超出范围')
table(num)
