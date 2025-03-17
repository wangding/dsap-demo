#!/usr/bin/env python

# 基于列表的队列
class ArrayQueue:
  DEFAULT_CAPACITY = 10

  def __init__(self):
    self.__A = [None] * ArrayQueue.DEFAULT_CAPACITY
    self.__n = 0    # 队列长度，队列容量：len(self.__A)
    self.__h = 0    # 队列头指针 head

  def __len__(self):  return self.__n
  def is_empty(self): return self.__n == 0
  def __repr__(self): return str(self.__A)

  def first(self):
    if self.__n == 0: raise Exception('队列为空')
    return self.__A[self.__h]

  def enqueue(self, e):
    if self.__n == len(self.__A): self.__resize(2 * len(self.__A))
    k = (self.__h + self.__n) % len(self.__A)
    self.__A[k] = e
    self.__n += 1

  def dequeue(self):
    if self.__n == 0: raise Exception('队列为空')
    answer = self.__A[self.__h]
    self.__A[self.__h] = None      # 便于演示，可以去掉
    self.__h = (self.__h + 1) % len(self.__A)
    self.__n -= 1
    return answer

  def __resize(self, n):
    B = [None] * n
    walk = self.__h
    for k in range(self.__n):
      B[k] = self.__A[walk]
      walk = (walk + 1) % len(self.__A)
    self.__A = B
    self.__h = 0