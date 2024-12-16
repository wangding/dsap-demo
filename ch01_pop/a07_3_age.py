#!/usr/bin/env python

# 异常捕获
# 不同的异常，相同的响应

age = -1

while age <= 0:
  try:
    age = int(input('Enter your age in years: '))
    if age <= 0:
      print('Your age must be positive')
  except (ValueError, EOFError):
    print('Invalid response')

# CTRL+Z => EOFError
