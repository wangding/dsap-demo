#!/usr/bin/env python

# 基于递归的累加求和
def summation(n):
  if n == 0: return 0
  return n + summation(n-1)

N = 100
print(f'1+2+...+{N} = {summation(N)}')
