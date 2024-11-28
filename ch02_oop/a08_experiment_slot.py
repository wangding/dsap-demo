#!/usr/bin/env python

# 实验验证普通实例空间 dict 管理标识符
# 比 __slots__ 管理标识符占更多的内存

import sys

class Node1:
  def __init__(self, name, age):
    self.name = name
    self.age  = age

class Node2:
  __slots__ = 'name', 'age'
  def __init__(self, name, age):
    self.name = name
    self.age  = age

size1 = sys.getsizeof(Node1('wangding', 20))
size2 = sys.getsizeof(Node2('wangding', 20))

print('size1:', size1, 'bytes')
print('size2:', size2, 'bytes')
print('size1 > size2:', size1 > size2)