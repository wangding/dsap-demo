#!/usr/bin/env python

# 自定义序列类，实现迭代器

class SequenceIterator:
  def __init__(self, sequence):
    self._seq = sequence
    self._k = -1

  def __next__(self):
    self._k += 1
    if self._k < len(self._seq):
      return(self._seq[self._k])
    else:
      raise StopIteration()

  def __iter__(self):
    return self

if __name__ == '__main__':
  str = SequenceIterator('abc')
  for c in str:
    print(c, end='')

  print()
  arr = SequenceIterator([1, 2, 3])
  for item in arr:
    print(item, end=',')

  print()
  num_set = SequenceIterator(('x', 'y', 'z'))
  for item in num_set:
    print(item, end=',')
