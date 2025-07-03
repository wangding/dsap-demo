#!/usr/bin/env python

# 猜数游戏
# 模拟策略三：随机查找，缩小范围

from random import randint

class Numbers():
  def __init__(self, start=1, end=100):
    self.__nums = list(range(start, end + 1))
    self.__low  = start
    self.__high = end

  def get(self):
    index = randint(0, self.__high - self.__low)
    nums = self.__nums[self.__low-1: self.__high]
    return nums[index]
  
  def set_low(self, low):   self.__low  = low
  def set_high(self, high): self.__high = high
  def __repr__(self):
    return 'low:  ' + str(self.__low) + '\n' + \
           'high: ' + str(self.__high) + '\n' + \
           'nums: ' + str(self.__nums[self.__low-1: self.__high])

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
      nums.set_low(guess+1)
    else:
      print(f'{n:2}: {guess:2} 不对。猜的数大了。')
      nums.set_high(guess-1)

game()
