#!/usr/bin/env python

# 猜数游戏，可以使用三种策略
# 策略一、逐个查找
# 策略二、折半查找
# 策略三、随机查找

from random import randint

def game():
  answer = randint(1, 100)
  print("猜数游戏，现在开始...")
  while True:
    guess = int(input("1~100 之间，请给出你的答案："))
    if guess == answer:
      print(f"太棒了！这个数就是 {answer}")
      break
    elif guess < answer: print('不对。你猜的数小了。')
    else: print('不对。你猜的数大了。')

game()
