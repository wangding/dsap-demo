#!/usr/bin/env python

def sum_squares(n):
  total = 0
  for i in range(n+1):
    total += i*i
  return total

print('1~5 sum of the squares:', sum_squares(5))