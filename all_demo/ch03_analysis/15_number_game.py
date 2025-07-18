#!/usr/bin/env python

# 猜数游戏
# 模拟策略三：随机查找，避免重复

from random import randint

class Numbers():
  def __init__(self, start=1, end=100):
    self.__nums = list(range(start, end + 1))

  def get(self):
    """获取一个随机数，并从列表中删除它"""
    index = randint(0, len(self.__nums) - 1)
    num = self.__nums[index]
    self.__nums[index] = self.__nums[-1]  # 用最后一个数替换
    self.__nums.pop()  # 删除最后一个数
    return num

  def __repr__(self): return str(self.__nums)

def game():
  answer = randint(1, 100)
  nums = Numbers()
  n = 0
  print("猜数游戏，现在开始...")
  while True:
    guess = nums.get()
    n += 1
    if guess == answer:
      print(f"\n太棒了！这个数就是 {answer}")
      break
    elif guess < answer:
      print(f'{n:2}: {guess:2} 不对。猜的数小了。')
    else:
      print(f'{n:2}: {guess:2} 不对。猜的数大了。')

game()
