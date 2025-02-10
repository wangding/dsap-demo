#!/usr/bin/env python

# 猜数游戏
# 模拟策略二：折半查找

from random import randint

def game():
  answer = randint(1, 100)
  print("猜数游戏，现在开始...")
  low, high = 1, 101
  while True:
    guess = (low+high)//2
    if guess == answer:
      print(f"\n太棒了！这个数就是 {answer}")
      break
    elif guess < answer:
      print(f'{guess} 不对。猜的数小了。')
      low = guess
    else:
      print(f'{guess} 不对。猜的数大了。')
      high = guess

game()