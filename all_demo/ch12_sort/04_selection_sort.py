#!/usr/bin/env python

def selection_sort(data):
  for j in range(len(data)-1):
    small, pos = data[j], 0
    for k in range(j, len(data)):
      if data[k] < small: small, pos = data[k], k
    data[j], data[pos] = small, data[j]

lst = [31, 41, 59, 26, 41, 58]
print('before sort:', lst)
selection_sort(lst)
print('after sort: ', lst)