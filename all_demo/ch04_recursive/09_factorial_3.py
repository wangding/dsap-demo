#!/usr/bin/env python

# 递归计算阶乘
def factorial(n):
  if n == 0: return 1
  f = factorial(n-1)
  return n * f

print('计算阶乘...')
num = int(input('请输入一个正整数：'))
print(f'{num}! = {factorial(num)}')
