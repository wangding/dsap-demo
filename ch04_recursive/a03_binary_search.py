#!/usr/bin/env python

# 递归二分查找

def binary_search(data, target, low, high):
  if low > high:
    return None
  else:
    mid = (low + high) // 2
    if target == data[mid]:
      return mid
    elif target < data[mid]:
      return binary_search(data, target, low, mid - 1)
    else:
      return binary_search(data, target, mid + 1, high)

if __name__ == '__main__':
  data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
  index = binary_search(data, 22, 0, len(data))
  print(f'data[{index}] = {data[index]}')
