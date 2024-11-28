#!/usr/bin/env python

# 自定义 Range 类，实现迭代器

class Range:
  def __init__(self, start, stop=None, step=1):
    if step == 0:
      raise ValueError('step cannot be 0')
      
    if stop is None:
      start, stop = 0, start

    self._length = max(0, (stop - start + step - 1) // step)

    self._start = start
    self._step = step

  def __len__(self):
    return self._length

  def __getitem__(self, k):
    if k < 0:
      k += len(self)

    if not 0 <= k < self._length:
      raise IndexError('index out of range')

    return self._start + k * self._step

if __name__ == '__main__':
  for i in Range(5):
    print(i, end=', ')

  print()
  for i in Range(-5, 0):
    print(i, end=', ')

  print()
  for i in Range(1, 10, 3):
    print(i, end=', ')
