#!/usr/bin/env python

# 随机点名
from random import randint
import os
def picker(lst):
  for num in range(1, len(lst)):
    i = randint(0, len(lst)-num)
    if os.name in ('nt', 'dos'): os.system('cls')
    else: os.system('clear')
    print(lst[i], end='')
    input()
    lst[i], lst[len(lst)-num] = lst[len(lst)-num], lst[i]

file = open('students.txt', 'r', encoding='utf_8')
names = file.read().split('\n')
picker(names)