#!/usr/bin/env python

def insert_sort(data):
  for x in range(1, len(data)):
    num = data[x]
    while x>0 and data[x-1] > num:
      data[x] = data[x-1]
      x -= 1
    data[x] = num

lst = [31, 41, 59, 26, 41, 58]
print('before sort:', lst)
insert_sort(lst)
print('after sort: ', lst)