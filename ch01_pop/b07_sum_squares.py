#!/usr/bin/env python

def sum_squares(n):
  return sum(x*x for x in range(1,n+1,2))

print('1~5 sum of the squares:', sum_squares(5))