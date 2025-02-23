#!/usr/bin/env python

from time import time

# 循环计算阶乘
def factorial(n):
  fct = 1
  for x in range(1, n+1): fct *= x
  return fct

print('计算阶乘...')
num = int(input('请输入一个正整数：'))
start = time()
print(f'{num}! = {factorial(num)}')
end   = time()
print(f'算法耗时：{end-start} s')
