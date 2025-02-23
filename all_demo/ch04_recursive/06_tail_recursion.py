#!/usr/bin/env python

# 尾递归调用
def fn(n):
  if n == 0: return
  print(n, end=' ')
  fn(n - 1)

fn(5)
