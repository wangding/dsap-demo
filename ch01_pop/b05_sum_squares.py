#!/usr/bin/env python

def sum_squares(n):
  return sum(x*x for x in range(n+1))

print('1~5 sum of the squares:', sum_squares(5))