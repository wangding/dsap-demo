#!/usr/bin/env python

# 求平方根
def sqrt(num):
  PRECISION = 0.01
  delta = 1
  low, high = (1, num) if num > 1 else (0, 1)
  while delta > PRECISION:
    root = (low+high) / 2
    if root ** 2 == num: break
    elif root ** 2 < num: low = root
    else: high = root
    delta = high - low
  return root

if __name__ == '__main__':
  number = float(input('计算平方根，请输入这个数字：'))
  print(f'sqrt({number}) = {sqrt(number)}')
