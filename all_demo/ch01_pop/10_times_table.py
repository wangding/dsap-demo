#!/usr/bin/env python

num = int(input('Please input num[1-9]: '))
if not 1<= num <= 9: raise Exception('num 超出范围')
for n in range(1, num+1):
  for m in range(1, n+1):
    if m==2 and (n==3 or n==4):
      print(f'{m}×{n}={m*n:<2}', end=' ')
    else:
      print(f'{m}×{n}={m*n}', end=' ')
  print('')
