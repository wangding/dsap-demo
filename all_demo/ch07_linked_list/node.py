#!/usr/bin/env python

class Node:
  __slots__ = 'elem', 'next'

  def __init__(self, element, next=None):
    self.elem = element
    self.next = next

  def __repr__(self):
    return str(self.elem) + ' -> ' + str(self.next)
