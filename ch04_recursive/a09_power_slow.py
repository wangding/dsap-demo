#!/usr/bin/env python

# 递归求 x^n

def power(x, n):
  if n == 0:
    return 1
  else:
    return x * power(x, n-1)

if __name__ == '__main__':
  print(f'3^4 = {power(3, 4)}')
