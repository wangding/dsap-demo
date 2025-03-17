#!/usr/bin/env python

# 乘二取整，十进制小数转二进制
from array_queue import ArrayQueue

def dec2bin(num, pre=50):
  q = ArrayQueue()
  while num !=0 and len(q)<pre:
    q.enqueue(int(num*2))
    num = num*2 - int(num*2)
  return '0.' + ''.join([str(q.dequeue()) for x in range(len(q))])

data = [0.1, 0.125, 0.2, 0.25, 0.4, 0.5, 0.625, 0.75]
for item in data: print(f'{item:5}', dec2bin(item))