#!/usr/bin/env python

# 生成斐波那契数列的函数
# 使用生成器，实现惰性计算
# 使用同时分配，改进代码风格，代码更简练

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a+b

fib = fibonacci()
for x in range(10):
  print(next(fib), end=' ')