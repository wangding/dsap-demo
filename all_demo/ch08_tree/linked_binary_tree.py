from array_queue import *

class LinkedBinaryTree:
  class __Node:
    __slots__ = 'elem', 'left', 'right'

    def __init__(self, element, left=None, right=None):
      self.elem  = element
      self.left  = left
      self.right = right

    def __repr__(self):
      return f'({str(self.elem)}, {self.left}, {self.right})'

  def __init__(self, data):
    self.__n = 0
    self.__r = self.__mktree(data)

  def __mktree(self, data):
    if data == None: return None
    elem, left, right = data
    self.__n += 1
    return self.__Node(elem, self.__mktree(left), self.__mktree(right))

  def __repr__(self): return str(self.__r)
  def __len__(self):  return self.__n
  def is_empty(self): return self.__n == 0
  def root(self):     return self.__r

  def preorder(self):
    for node in self.__preorder(self.__r): yield node
    # print()

  def inorder(self):
    self.__inorder(self.__r)
    print()

  def postorder(self):
    self.__postorder(self.__r)
    print()

  def __preorder(self, node):
    if node == None: return
    # print(node.elem, end=' ')
    yield node
    for n in self.__preorder(node.left):  yield n
    for n in self.__preorder(node.right): yield n

  def __inorder(self, node):
    if node == None: return
    self.__inorder(node.left)
    print(node.elem, end=' ')
    self.__inorder(node.right)

  def __postorder(self, node):
    if node == None: return
    self.__postorder(node.left)
    self.__postorder(node.right)
    print(node.elem, end=' ')

  def breadth_first(self):
    if self.__r == None: return
    q = ArrayQueue()
    q.enqueue(self.__r)
    while len(q)>0:
      node = q.dequeue()
      if node == None: continue
      print(node.elem, end=' ')
      q.enqueue(node.left)
      q.enqueue(node.right)
    print()

if __name__ == '__main__':
  t = LinkedBinaryTree((1, (2, (4, None, None), (5, None, None)), (3, None, None)))
  # for node in t.preorder(): print(node.elem)
  t.breadth_first()