#!/usr/bin/env python

# 紧凑数组的用法
from array import array

data = array('b', b'hello world')
print('type code:', data.typecode)
print('item size:', data.itemsize)
print('(addr, total size):', data.buffer_info())
for c in data: print(c, end=' ')
print()
for c in data: print(chr(c), end='')
