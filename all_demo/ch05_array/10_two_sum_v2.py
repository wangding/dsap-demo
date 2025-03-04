#!/usr/bin/env python

# 两数求和
def two_sum(nums, target):
  buf = {}
  for i, num in enumerate(nums):
    if target - num in buf: return i, buf[target-num]
    buf[num] = i
  return None

nums = [2, 7, 11, 15]
target = 9
# nums = [3,2,4]
# target = 6
# nums = [3,3]
# target = 6
print(two_sum(nums, target))