#!/usr/bin/env python

# 数组乱序
from random import randint
def suffle(lst):
  for num in range(1, len(lst)):
    i = randint(0, len(lst)-num)
    lst[i], lst[len(lst)-num] = lst[len(lst)-num], lst[i]

s = [1, 2, 3, 4, 5]
print(s)
suffle(s)
print(s)