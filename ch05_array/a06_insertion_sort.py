#!/usr/bin/env python

# 插入排序

def insertion_sort(A):
  for k in range(1, len(A)):
    cur = A[k]
    j = k
    while j > 0 and A[j-1] > cur:
      A[j] = A[j-1]
      j -= 1
    A[j] = cur

if __name__ == '__main__':
  data = [5, 2, 8, 1, 4]
  print('before:', data)
  insertion_sort(data)
  print('after: ', data)
  
