#!/usr/bin/env python

# 扫雷游戏
from random import randint
import os

class MinesGame():
  def __init__(self, level=0):
    if not 0<= level < 3: raise Exception('游戏级别不合法')
    self.__level = level
    self.__board_be = []
    self.__board_fe = []
    self.__init_board()
    self.__set_mines()
    self.__set_numbers()
    self.__isWin  = False
    self.__isFail = False
    # self.__print_board_be()

  __row_col  = [(9,9), (16,16), (16,30)]
  __mines    = [10, 40, 99]
  __cells    = [m*n for m,n in __row_col]
  __chars_be = '０１２３４５６７８＊'
  __chars_fe = '🟦⬜🚩💣💥'
  __chars    = '０１２３４５６７８９ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'

  def __init_board(self):
    n, m = MinesGame.__row_col[self.__level]
    self.__board_be = [[0]*m for k in range(n)]
    self.__board_fe = [[0]*m for k in range(n)]

  def __get_x_y(self, num):
    n, m = MinesGame.__row_col[self.__level]
    return (num//m, num % m)

  def __set_mines(self):
    mines = MinesGame.__mines[self.__level]
    nums = MinesGame.__cells[self.__level]
    cells = list(x for x in range(nums))
    for n in range(mines):
      k = randint(0, nums-n-1)
      x, y = self.__get_x_y(cells[k])
      self.__board_be[x][y] = 9
      cells[k], cells[-1*(n+1)] = cells[-1*(n+1)], cells[k]

  def __set_numbers(self):
    b = self.__board_be
    row, col = MinesGame.__row_col[self.__level]
    directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
    for n in range(row):
      for m in range(col):
        if b[n][m] != 9: continue
        for x,y in directions:
          r, c = n+x, m+y
          if 0<= r < row and 0<= c < col and b[r][c] !=9: b[r][c] +=1

  def __print_board_be(self):
    chars = MinesGame.__chars_be
    board = self.__board_be
    for n in range(len(board)):
      for m in range(len(board[0])):
        print(chars[board[n][m]], end='')
      print()

  def __print_board(self):
    row, col = MinesGame.__row_col[self.__level]
    if os.name in ('nt', 'dos'): os.system('cls')
    else: os.system('clear')
    print('　' + self.__chars[:col])
    for n in range(row):
      print(MinesGame.__chars[n], end='')
      for m in range(col):
        if self.__board_fe[n][m] == 1 and self.__board_be[n][m] != 0:
          print(MinesGame.__chars_be[self.__board_be[n][m]], end='')
        else:
          print(MinesGame.__chars_fe[self.__board_fe[n][m]], end='')
      print('')

  def __game_over(self): return self.__isFail or self.__isWin
  
  def __flag(self, n, m):
    b = self.__board_fe
    # 没有翻开的地块0，标上🚩2；标上🚩2的地块，恢复成0；翻开的地块1，忽略
    b[n][m] = {0:2, 2:0}.get(b[n][m], b[n][m])

  def __dig(self, n, m):
    row, col = MinesGame.__row_col[self.__level]
    if self.__board_fe[n][m] != 0: return    # 只能挖没有翻开的地块0，如果当前地块已翻开，啥也不做

    if self.__board_be[n][m] == 9:           # 当前地块下面是地雷
      self.__isFail = True         # 设置游戏失败状态
      for i in range(row):
        for j in range(col):
          if self.__board_be[i][j] == 9: self.__board_fe[i][j] = 3   # 设置有雷地块💣标记3
      self.__board_fe[n][m] = 4    # 设置当前地块💥标记4
      return

    self.__board_fe[n][m] = 1      # 设置当前地块已经翻开1

    if self.__board_be[n][m] !=0: return  # 如果当前地块下面是数字，不用向周围扩展挖掘

    directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
    for x, y in directions:        # 向周围八个方向扩展挖掘
      r, c = n+x, m+y
      if 0<= r < row and 0<= c < col: self.__dig(r, c)

  def __judgeWin(self):
    if self.__isFail: return  # 游戏已经失败，就不用再判断胜负了
    board_be = [[int(x != 9) for x in row] for row in self.__board_be]
    board_fe = [[int(x == 1) for x in row] for row in self.__board_fe]
    self.__isWin = board_be == board_fe

  def play(self):
    self.__print_board()
    while not self.__game_over():
      try:
        cmd, n, m = input('操作：d,n,m：挖雷，f,n,m：标雷。\n请输入: ').split(',')
        n, m = int(n), int(m)
      except ValueError: continue
      r, c = self.__row_col[self.__level]
      if not 0<= n < r or not 0<= m < c: continue
      if cmd.lower() == 'f': self.__flag(n, m)
      if cmd.lower() == 'd': self.__dig(n, m)
      self.__judgeWin()            # 评判游戏胜负
      self.__print_board()         # 重画游戏画面
    if self.__isWin:  print('恭喜你，扫雷成功！🎉')
    if self.__isFail: print('你踩到雷了！扫雷失败！😭')

level = None
msg = '欢迎进入扫雷游戏！\n' + \
      '游戏有三种难度等级：\n' + \
      '  0：初级难度， 9×9  个地块，10 个雷\n' + \
      '  1：中级难度，16×16 个地块，40 个雷\n' + \
      '  2：高级难度，16×30 个地块，99 个雷'
while True:
  if os.name in ('nt', 'dos'): os.system('cls')
  else: os.system('clear')
  print(msg)
  try:
    level = int(input('请选择游戏难度[0-2]：'))
    if 0<= level < 3: break
  except ValueError: continue
game = MinesGame(level)
game.play()
