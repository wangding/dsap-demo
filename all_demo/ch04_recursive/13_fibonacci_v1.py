#!/usr/bin/env python

# 两路递归求斐波那契数列
def fibonacci(n):
  if n <= 1: return n
  return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(6))
