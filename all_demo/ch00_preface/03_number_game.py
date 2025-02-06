#!/usr/bin/env python

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
