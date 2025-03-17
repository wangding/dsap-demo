#!/usr/bin/env python

# 基于数组的栈
class ArrayStack:
  def __init__(self): self.__A = []
  def __len__(self):  return len(self.__A)
  def is_empty(self): return len(self.__A) == 0
  def push(self, e):  self.__A.append(e)
  def __repr__(self): return str(self.__A)

  def pop(self):
    if self.is_empty(): raise Exception('栈为空')
    return self.__A.pop()

  def top(self):
    if self.is_empty(): raise Exception('栈为空')
    return self.__A[-1]
