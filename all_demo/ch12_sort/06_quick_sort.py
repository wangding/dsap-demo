#!/usr/bin/env python

def quick_sort(arr):
  if len(arr) <= 1: return arr
  pivot = arr[0]
  left  = [x for x in arr[1:] if x < pivot]
  right = [x for x in arr[1:] if x >= pivot]
  return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
  data = [34, 7, 23, 32, 5, 62]
  print("排序前:", data)
  sorted_data = quick_sort(data)
  print("排序后:", sorted_data)