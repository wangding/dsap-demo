#!/usr/bin/env python

from doubly_linked_base import DoublyLinkedBase

class LinkedDeque(DoublyLinkedBase):
  def first(self):
    if self.is_empty(): raise Exception("队列为空")
    return self._h.next.elem

  def last(self):
    if self.is_empty(): raise Exception("队列为空")
    return self._t.prev.elem

  def add_first(self, e): self._insert_between(e, self._h, self._h.next)
  def add_last(self, e):  self._insert_between(e, self._t.prev, self._t)

  def del_first(self):
    if self.is_empty(): raise Exception("队列为空")
    return self._delete_node(self._h.next)

  def del_last(self):
    if self.is_empty(): raise Exception("队列为空")
    return self._delete_node(self._t.prev)
