#!/usr/bin/env python

# 用栈进行括号匹配检测
from array_stack import ArrayStack

def is_matched(expr):
  lefty, righty = '({[', ')}]'
  stack = ArrayStack()
  for c in expr:
    if c in lefty: stack.push(c)
    if c in righty:
      if stack.is_empty(): return False
      if righty.index(c) != lefty.index(stack.pop()): return False
  return stack.is_empty()

data = ['[(5+x)*(y-z)]', '[(5+x)*(y-z}]', '[(5+x)*(y-z)])', '[(5+x)*(y-z)']
for item in data: print(f'{item:15}', is_matched(item))