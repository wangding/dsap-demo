#!/usr/bin/env python

# 用栈对文件逆序

from a01_array_stack import ArrayStack

def reverse_file(filename):
  S = ArrayStack()
  original = open(filename)       
  for line in original:
    S.push(line.rstrip('\n'))
  original.close()

  output = open(filename, 'w')
  while not S.is_empty():
    output.write(S.pop() + '\n')
  output.close()

if __name__ == '__main__':
  f = open('test.txt', 'w')
  f.write('1. hello\n2. world\n3. wang\n4. ding')
  f.close()
  reverse_file('test.txt')
