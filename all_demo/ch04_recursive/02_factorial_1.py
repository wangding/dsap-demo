#!/usr/bin/env python

# 递归计算阶乘
def factorial(n):
  return 1 if n == 0 else n * factorial(n - 1)

print('计算阶乘...')
num = int(input('请输入一个正整数：'))
print(f'{num}! = {factorial(num)}')
