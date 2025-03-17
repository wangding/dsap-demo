#!/usr/bin/env python

from array_queue import ArrayQueue

# 基于队列的栈
class QueueStack:
  def __init__(self): self.__data = ArrayQueue()
  def __len__(self):  return len(self.__data)
  def is_empty(self): return self.__data.is_empty()
  def push(self, e):  self.__data.enqueue(e)

  def pop(self):
    if self.is_empty(): raise Exception('栈为空')
    for k in range(len(self)-1): self.__data.enqueue(self.__data.dequeue())
    return self.__data.dequeue()

  def top(self):
    if self.is_empty(): raise Exception('栈为空')
    for k in range(len(self)-1): self.__data.enqueue(self.__data.dequeue())
    answer = self.__data.dequeue()
    self.__data.enqueue(answer)
    return answer
