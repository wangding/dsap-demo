#!/usr/bin/env python

# 递归计算 n!

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

if __name__ == '__main__':
  print(f'5! = {factorial(5)}')
