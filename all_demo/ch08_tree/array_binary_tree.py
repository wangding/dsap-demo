from array_queue import *

class ArrayBinaryTree:
  def __init__(self, data):
    self.__A = []
    self.__mktree(data)

  def __repr__(self): return str(self.__A)
  def __len__(self):  return len(self.__A)
  def is_empty(self): return len(self) == 0

  def __mktree(self, data):
    if data == None: return
    q = ArrayQueue()
    q.enqueue(data)
    while len(q)>0:
      elem, left, right = q.dequeue()
      self.__A.append(elem)
      if left != None: q.enqueue(left)
      if right != None: q.enqueue(right)