#!/usr/bin/env python

class LinkedQueue:
  class __Node:
    __slots__ = 'elem', 'next'
    def __repr__(self): return str(self.elem) + ' -> ' + str(self.next)
    def __init__(self, element, next):
      self.elem = element
      self.next = next

  def __init__(self): self.__h, self.__t, self.__n = None, None, 0
  def __len__(self):  return self.__n
  def is_empty(self): return self.__n == 0
  def __repr__(self): return str(self.__h)

  def first(self):
    if self.__n == 0: raise Exception('队列为空')
    return self.__h.elem

  def dequeue(self):
    if self.__n == 0: raise Exception('队列为空')
    data = self.__h.elem
    self.__h  = self.__h.next
    self.__n -= 1
    if self.__n == 0: self.__t = None
    return data

  def enqueue(self, e):
    newest = self.__Node(e, None)
    if self.__n == 0: self.__h = newest
    else: self.__t.next = newest
    self.__t = newest
    self.__n += 1