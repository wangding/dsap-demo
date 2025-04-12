#!/usr/bin/env python

class CircularQueue:
  class __Node:
    __slots__ = 'elem', 'next'
    def __init__(self, element, next):
      self.elem = element
      self.next = next

  def __init__(self): self.__t, self.__n = None, 0
  def __len__(self):  return self.__n
  def is_empty(self): return self.__n == 0

  def first(self):
    if self.__n == 0: raise Exception('队列为空')
    node = self.__t.next
    return node.elem

  def dequeue(self):
    if self.__n == 0: raise Exception('队列为空')
    oldhead = self.__t.next
    if self.__n == 1: self.__t = None
    else: self.__t.next = oldhead.next
    self.__n -= 1
    return oldhead.elem

  def enqueue(self, e):
    newest = self.__Node(e, None)
    if self.__n == 0: newest.next = newest
    else:
      newest.next = self.__t.next
      self.__t.next = newest
    self.__t = newest
    self.__n += 1

  def rotate(self):
    if self.__n == 0: raise Exception('队列为空')
    self.__t = self.__t.next

  def __repr__(self):
    if self.__n == 0: return ''
    node, data = self.__t.next, []
    for k in range(len(self)):
      data.append(node.elem)
      node = node.next
    return ' -> '.join(str(x) for x in data)