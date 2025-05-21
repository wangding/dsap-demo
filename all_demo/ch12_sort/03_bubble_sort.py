#!/usr/bin/env python

def bubble_sort(data):
  for j in range(len(data)):
    for k in range(len(data) - j - 1):
      if data[k] > data[k+1]: data[k], data[k+1] = data[k+1], data[k]

lst = [31, 41, 59, 26, 41, 58]
print('before sort:', lst)
bubble_sort(lst)
print('after sort: ', lst)