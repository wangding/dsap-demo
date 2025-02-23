#!/usr/bin/env python

# 循环计算阶乘
def factorial(n):
  fct = 1
  for x in range(1, n+1): fct *= x
  return fct

print('计算阶乘...')
num = int(input('请输入一个正整数：'))
print(f'{num}! = {factorial(num)}')
