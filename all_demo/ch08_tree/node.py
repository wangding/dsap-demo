#!/usr/bin/env python

class Node:
  __slots__ = 'elem', 'left', 'right'

  def __init__(self, element, left=None, right=None):
    self.elem  = element
    self.left  = left
    self.right = right

  def __repr__(self):
    return f'({str(self.elem)}, {self.left}, {self.right})'
