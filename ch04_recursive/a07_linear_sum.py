#!/usr/bin/env python

# 线性递归求和

def linear_sum(S, n):
  if n == 0:
    return 0
  else:
    return linear_sum(S, n-1) + S[n-1]

if __name__ == '__main__':
  data = [1, 2, 3, 4, 5]
  total = linear_sum(data, len(data))
  print(f'sum({data}) = {total}')
