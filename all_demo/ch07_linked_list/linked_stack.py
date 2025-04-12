#!/usr/bin/env python

class LinkedStack:
  class __Node:
    __slots__ = 'elem', 'next'
    def __repr__(self): return str(self.elem) + ' -> ' + str(self.next)
    def __init__(self, element, next):
      self.elem = element
      self.next = next

  def __init__(self): self.__h, self.__n = None, 0
  def __len__(self):  return self.__n
  def is_empty(self): return self.__n == 0
  def __repr__(self): return str(self.__h)

  def push(self, e):
    self.__h =  self.__Node(e, self.__h)
    self.__n += 1

  def top(self):
    if self.__n == 0: raise Exception('栈为空')
    return self.__h.elem

  def pop(self):
    if self.is_empty(): raise Exception('栈为空')
    data = self.__h.elem
    self.__h = self.__h.next
    self.__n -= 1
    return data