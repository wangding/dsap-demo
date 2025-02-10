#!/usr/bin/env python

# 猜数游戏
# 模拟策略一：逐个查找

from random import randint

def game():
  answer = randint(1, 100)
  guess = 0
  print("猜数游戏，现在开始...")
  while True:
    guess += 1
    if guess == answer:
      print(f"\n太棒了！这个数就是 {answer}")
      break
    if guess < answer: print(f'{guess:2} 不对。猜的数小了。')
    else: print(f'{guess:2} 不对。你猜的数大了。')

game()
