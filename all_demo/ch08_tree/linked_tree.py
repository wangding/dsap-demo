from array_queue import *

class LinkedTree:
  class __Node:
    __slots__ = 'elem', 'children'

    def __init__(self, element):
      self.elem = element 
      self.children = []

    def __repr__(self):
      return f'({str(self.elem)}, {str(self.children)})'
  
  def __init__(self, data):
    self.__n = 0
    self.__r = self.__mktree(data)

  def __len__(self):  return self.__n
  def is_empty(self): return self.__n == 0
  def __repr__(self): return str(self.__r)
  def preorder(self): self.__preorder(self.__r)

  def breadth_first(self):
    if self.__r == None: return
    q = ArrayQueue()
    q.enqueue(self.__r)
    while len(q)>0:
      node = q.dequeue()
      if node == None: continue
      print(node.elem)
      for child in node.children: q.enqueue(child)

  def __mktree(self, data):
    if len(data) == 0: return None
    n = self.__Node(data[0])
    data.pop(0)
    if len(data) != 0:
      for item in data: n.children.append(self.__mktree(item))
    return n

  def __preorder(self, node, deepth=0):
    if node == None: return
    print(' '*2*deepth+node.elem)
    for child in node.children: self.__preorder(child, deepth+1)

if __name__ == '__main__':
  data = ['Paper',
                  ['Title'],
                  ['Abstract'],
                  ['$1', ['$1.1'], ['$1.2']],
                  ['$2', ['$2.1'], ['$2.2'], ['$2.3']],
                  ['$3', ['$3.1'], ['$3.2']], ['Reference']]
  t = LinkedTree(data)
  print(t)
  # t.breadth_first()
  t.preorder()