#!/usr/bin/env python

def min_max(arr):
  min = max = arr[0]
  for val in arr:
    if val < min:
      min = val
    if val > max:
      max = val
  return min, max

min, max = min_max([1, 5, 3, 2, 4])

print('1, 5, 3, 2, 4')
print(f'min = {min}')
print(f'max = {max}')