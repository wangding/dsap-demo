#!/usr/bin/env python

# 用栈逆序队列
from array_stack import ArrayStack

def reverse(data):
  stack = ArrayStack()
  for x in data: stack.push(x)
  return [stack.pop() for x in range(len(data))]

data = [3, 2, 5, 1, 4]
print('before:', data)
print('after: ', reverse(data))
