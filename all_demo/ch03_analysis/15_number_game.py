#!/usr/bin/env python

# 猜数游戏
# 模拟策略三：随机查找，避免重复

from random import randint

def game():
  answer = randint(1, 100)
  nums = list(range(1,101))
  print("猜数游戏，现在开始...")
  while True:
    index = randint(0, len(nums)-1)
    guess = nums.pop(index)
    if guess == answer:
      print(f"\n太棒了！这个数就是 {answer}")
      break
    elif guess < answer:
      print(f'{guess:2} 不对。猜的数小了。')
    else:
      print(f'{guess:2} 不对。猜的数大了。')

game()
