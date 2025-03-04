#!/usr/bin/env python

# 两数求和
def two_sum(nums, target):
  for x in range(len(nums)):
    for y in range(x+1, len(nums)):
      if nums[x] + nums[y] == target: return x, y
  return None

# nums = [2, 7, 11, 15]
# target = 9
# nums = [3, 2, 4]
# target = 6
nums = [3, 3]
target = 6
print(two_sum(nums, target))