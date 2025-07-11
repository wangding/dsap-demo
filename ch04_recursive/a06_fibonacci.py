#!/usr/bin/env python

# 两路递归和线性递归求斐波那契数列

def bad_fibonacci(n):
  if n <= 1:
    return n
  else:
    return bad_fibonacci(n-2) + bad_fibonacci(n-1)

def good_fibonacci(n):
  if n <= 1:
    return (n, 0)
  else:
    (a, b) = good_fibonacci(n-1)
    return (a+b, a)

if __name__ == '__main__':
  print(bad_fibonacci(5))
  print(good_fibonacci(5))
