#!/usr/bin/env python

# 线性递归逆序

def reverse(S, start, stop):
  if start < stop - 1:
    S[start], S[stop-1] = S[stop-1], S[start]
    reverse(S, start+1, stop-1)

if __name__ == '__main__':
  data = [1, 2, 3, 4, 5]
  print('before:', data)
  reverse(data, 0, len(data))
  print('after: ', data)
