#!/usr/bin/env python

def times_table(m):
  def expr(a, b): return f'{a}×{b}={a*b}'
  def line(n):   return ' '.join([expr(a,n) for a in range(1,n+1)])
  return '\n'.join([line(n) for n in range(1,m+1)])

if __name__ == "__main__":
  num = int(input('Please input num[1-9]: '))
  if not 1<= num <= 9: raise Exception('num 超出范围')
  print(times_table(num))
