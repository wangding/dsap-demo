#!/usr/bin/env python

# 除二取余，十进制整数转二进制
from array_stack import ArrayStack

def dec2bin(num):
  s = ArrayStack()
  while num != 0:
    s.push(num % 2)
    num = num // 2
  return ''.join([str(s.pop()) for x in range(len(s))])

data = [1, 2, 3, 4, 5, 55, 32, 23, 8]
for item in data: print(f'({item:2})10 = ({dec2bin(item)})2')