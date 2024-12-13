#!/usr/bin/env python

# 递归测试元素唯一性

def unique(S, start, stop):
  if stop - start <= 1: return True
  elif not unique(S, start, stop-1): return False
  elif not unique(S, start+1, stop): return False
  else: return S[start] != S[stop-1]

if __name__ == '__main__':
  data1 = [1, 2, 3, 4]
  data2 = [1, 2, 3, 2]
  print(f'{data1} unique: {unique(data1, 0, len(data1))}')
  print(f'{data2} unique: {unique(data2, 0, len(data2))}')
