#!/usr/bin/env python

# 数组操作
lst = [3, 4, 1, 5, 2]

print('\ninsert:')
lst.insert(0, 77)        # at head
print(lst)
lst.insert(3, 88)        # at middle
print(lst)
lst.insert(len(lst), 99) # at tail
print(lst)

print('\nremove:')
lst.remove(77)          # at head
print(lst)
lst.remove(88)          # at middle
print(lst)
lst.remove(99)          # at tail
print(lst)

print('\nsort:')
lst.sort()
print(lst)