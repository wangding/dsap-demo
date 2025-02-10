#!/usr/bin/env python

# 猜数游戏
# 模拟策略三：随机查找

from random import randint

def game():
  answer = randint(1, 100)
  print("猜数游戏，现在开始...")
  while True:
    guess = randint(1, 100)
    if guess == answer:
      print(f"\n太棒了！这个数就是 {answer}")
      break
    elif guess < answer:
      print(f'{guess:2} 不对。猜的数小了。')
    else:
      print(f'{guess:2} 不对。猜的数大了。')

game()
