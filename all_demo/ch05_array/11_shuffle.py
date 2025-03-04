#!/usr/bin/env python

# 数组乱序
from random import randint
def suffle(lst):
  result, num = [], 0          # num 用来监视循环的次数
  while len(result)<len(lst):
    num += 1
    i = randint(0, len(lst)-1)
    if lst[i] not in result: result.append(lst[i])
  print(num)
  return result

s = [1, 2, 3, 4, 5]
print(s)
print(suffle(s))