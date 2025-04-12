#!/usr/bin/env python

class DoublyLinkedBase:
  class __Node:
    __slots__ = 'elem', 'prev', 'next'
    def __init__(self, element, prev, next):
      self.elem = element
      self.prev = prev
      self.next = next

  def __init__(self):
    self._h = self.__Node('BEGIN', None, None)
    self._t = self.__Node('END', None, None)
    self._h.next = self._t
    self._t.prev = self._h
    self.__n = 0

  def __len__(self):  return self.__n
  def is_empty(self): return self.__n == 0

  def _insert_between(self, e, predecessor, successor):
    newest = self.__Node(e, predecessor, successor)
    predecessor.next = newest
    successor.prev = newest
    self.__n += 1
    return newest

  def _delete_node(self, node):
    predecessor = node.prev
    successor = node.next
    predecessor.next = successor
    successor.prev = predecessor
    self.__n -= 1
    data = node.elem
    node.prev = node.next = node.elem = None
    return data

  def __repr__(self):
    data = []
    if self.__n == 0: return 'BEGIN <=> END'
    node = self._h.next
    for k in range(len(self)):
      data.append(node.elem)
      node = node.next
    return 'BEGIN <=> %s <=> END' % ' <=> '.join([str(x) for x in data])
