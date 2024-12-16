#!/usr/bin/env python

# 计算一个数的所有因子的函数
# 使用生成器，实现惰性计算
# 改进算法，计算速度更快，但是因子是乱序的

def factors(n):
  k = 1
  while k * k < n:
    if n % k == 0:
      yield k
      yield n // k
    k += 1
  if k * k == n:
    yield k

print([x for x in factors(7)])
print([x for x in factors(8)])
