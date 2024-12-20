#!/usr/bin/env python

# 用栈进行括号匹配检测

from a01_array_stack import ArrayStack

def is_matched(expr):
  lefty = '({['
  righty = ')}]'
  S = ArrayStack()
  for c in expr:
    if c in lefty:
      S.push(c)
    elif c in righty:
      if S.is_empty():
        return False
      if righty.index(c) != lefty.index(S.pop()):
        return False
  return S.is_empty()

if __name__ == '__main__':
  data = [
    '{()()[]}',
    '({[])}'
  ]
  for item in data:
    print(f'{item:10}', is_matched(item))