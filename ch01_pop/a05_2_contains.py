#!/usr/bin/env python

# 函数的 return 语句

def contains(data, target):
  for item in data:
    if item == target:
      return True
  return False

print(contains([29, 13, 'cron', 3.14], 'cron'))
print(contains([29, 13, 'cron', 3.14], 'gold'))
