#!/usr/bin/env python

# 线性递归求斐波那契数列
def fibonacci(n):
  if n == 1: return 1, 0
  a, b = fibonacci(n-1)
  return a+b, a

print(fibonacci(6))
