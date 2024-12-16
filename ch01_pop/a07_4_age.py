#!/usr/bin/env python

# 异常捕获
# 不同的异常，不同的响应
# 捕获异常后，再次抛出

age = -1
while age <= 0:
  try:
    age = int(input('Enter your age in years: '))
    if age <= 0:
      print('Your age must be positive')
  except ValueError:
    print('That is an invalid age specification')
  except EOFError:
    print('There was an unexpected error reading input.')
    raise

# CTRL+Z => EOFError
