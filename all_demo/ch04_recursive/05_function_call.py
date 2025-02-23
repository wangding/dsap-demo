#!/usr/bin/env python

# 普通函数调用
def fn2():
  print(5, end=' ')

def fn1():
  print(3, end=' ')
  fn2()
  print(4, end=' ')

def main():
  print(1, end=' ')
  fn1()
  print(2, end=' ')

main()
