#!/usr/bin/env python

# 求平方根
def sqrt(num):
  PRECISION, delta = 0.001, 1
  low, high = (1, num) if num > 1 else (0, 1)
  while delta > PRECISION:
    root = (low+high) / 2
    if root ** 2 == num: break
    elif root ** 2 < num: low = root
    else: high = root
    delta = high - low
  return root

print(sqrt(9))
print(sqrt(5))
print(sqrt(0.01))
