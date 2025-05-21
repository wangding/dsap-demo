#!/usr/bin/env python

def merge_sort(arr):
  if len(arr) <= 1: return arr
  mid = len(arr) // 2
  left  = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  return merge(left, right)

def merge(left, right):
  result, i, j = [], 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left [i:])
  result.extend(right[j:])
  return result

if __name__ == "__main__":
  left = [1, 4, 7]
  right = [2, 3, 8, 9]
  print("合并前:", left, right)
  merged = merge(left, right)
  print("合并后:", merged)

  arr = [38, 27, 43, 3, 9, 82, 10]
  print("\n排序前:", arr)
  sorted_arr = merge_sort(arr)
  print("排序后:", sorted_arr)