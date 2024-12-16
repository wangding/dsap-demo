#!/usr/bin/env python

# 计算一个数的所有因子的函数
# 传统方法

def factors(n):
  results = []
  for k in range(1, n+1):
    if n % k == 0:
      results.append(k)
  return results 

print(factors(7))
print(factors(8))
