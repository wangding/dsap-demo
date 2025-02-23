#!/usr/bin/env python

# 头递归调用
def fn(n):
  if n == 0: return
  fn(n - 1)
  print(n, end=' ')

fn(5)
