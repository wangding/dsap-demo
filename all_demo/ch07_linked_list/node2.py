#!/usr/bin/env python

class Node:
  __slots__ = 'elem', 'next', 'prev'

  def __init__(self, element, next=None, previous=None):
    self.elem = element
    self.next = next
    self.prev = previous

  def __repr__(self):
    return str(self.elem) + ' <=> ' + str(self.next)
