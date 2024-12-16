#!/usr/bin/env python

# 生成斐波那契数列的函数
# 使用生成器，实现惰性计算

def fibonacci():
  a = 0
  b = 1
  while True:
    yield a
    future = a + b
    a = b
    b = future

fib = fibonacci()
for x in range(10):
  print(next(fib), end=' ')
