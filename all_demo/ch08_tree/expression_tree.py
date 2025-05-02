from array_stack import *

class ExpressionTree:
  class __Node:
    __slots__ = 'elem', 'left', 'right'
    def is_leaf(self): return self.left == None and self.right == None

    def __init__(self, element, left=None, right=None):
      self.elem  = element
      self.left  = left
      self.right = right

    def __repr__(self):
      return f'({str(self.elem)}, {self.left}, {self.right})'

  def __init__(self, exp): self.__r = self.__build(exp)
  def __repr__(self): return str(self.__r)
  def eval(self): return self.__eval(self.__r)

  def preorder(self):
    self.__preorder(self.__r)
    print()

  def inorder(self):
    self.__inorder(self.__r)
    print()

  def postorder(self):
    self.__postorder(self.__r)
    print()

  def __eval(self, node):
    # 如果 node 是叶子则返回值
    # 如果 node 不是叶子则先计算，再返回计算结果
    if node.is_leaf(): return node.elem
    left  = self.__eval(node.left)
    right = self.__eval(node.right)
    opt = node.elem
    exp = '%s %s %s' % (left, opt, right)
    return eval(exp)

  def __build(self, exp):
    # 1 如果是 left value 则入栈 node
    # 2 如果是 opt(+-*/) 则入栈
    # 3 如果是 left value 则入栈 node
    # 如果是 ) 则出栈 1 2 3，构造 node 入栈
    s = ArrayStack()
    for c in exp:
      if c not in '+-*/()': s.push(self.__Node(c))
      if c in '+-*/': s.push(c)
      if c == ')':
        right = s.pop()
        opt = s.pop()
        left = s.pop()
        s.push(self.__Node(opt, left, right))
    return s.pop()

  def __preorder(self, node):
    if node == None: return
    print(node.elem, end=' ')
    self.__preorder(node.left)
    self.__preorder(node.right)
  
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

if __name__ == '__main__':
  exp = '(((3+1)*3)/((9-5)+2))'
  t = ExpressionTree(exp)
  print(t)
  print(t.eval())
  t.preorder()  # 前缀表达式
  t.inorder()   # 中缀表达式
  t.postorder() # 后缀表达式