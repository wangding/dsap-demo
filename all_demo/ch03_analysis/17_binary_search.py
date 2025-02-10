#!/usr/bin/env python

# 折半查找
def binary_search(data, target):
  low, high = 0, len(data)-1
  while low <= high:
    mid = (low+high)//2
    if data[mid] == target: return mid
    if data[mid] < target:  low = mid + 1
    else: high = mid - 1
  return None

data = [1, 2, 3, 5, 6, 7, 8]
print(f'data = {data}')
print(binary_search(data, 6))
print(binary_search(data, 9))
