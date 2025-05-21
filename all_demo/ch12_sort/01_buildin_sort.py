#!/usr/bin/env python

# list.sort()
src = [31, 41, 59, 26, 41, 58]
lst = src[:]
print('before sort:', src)
lst.sort()
print('after sort: ', lst)

# sorted()
print('\nbefore sort:', src)
print('after sort: ', sorted(src))

# reverse
print('\nbefore sort:', src)
print('after sort: ', sorted(src, reverse=True))

# key function
src = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']
print('before sort:', src)
print('after sort: ', sorted(src))
print('after sort: ', sorted(src, key=len))
