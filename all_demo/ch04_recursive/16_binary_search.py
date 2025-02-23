#!/usr/bin/env python

# 递归二分查找
def binary_search(data, target, low, high):
  mid = (low + high) // 2
  if low > high: return None
  if data[mid] == target: return mid
  if data[mid] >  target:
    return binary_search(data, target, low, mid-1)
  else:
    return binary_search(data, target, mid+1, high)

data = [2, 4, 5, 7, 8, 9]
index = binary_search(data, 5, 0, len(data))
print(f'index = {index}')
