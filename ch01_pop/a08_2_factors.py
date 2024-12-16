#!/usr/bin/env python

# 计算一个数的所有因子的函数
# 使用生成器，实现惰性计算

def factors(n):
  for k in range(1,n+1):
    if n % k == 0:
      yield k

print([x for x in factors(7)])
print([x for x in factors(8)])
