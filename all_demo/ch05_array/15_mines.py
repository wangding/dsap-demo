#!/usr/bin/env python

# 扫雷游戏
from random import randint

class MinesGame():
  def __init__(self, level=0):
    if not 0<= level < 3: raise Exception('游戏级别不合法')
    self.__level = level
    self.__board_be = []
    self.__init_board()
    # self.__print_board_be()
    self.__set_mines()
    # self.__print_board_be()
    self.__set_numbers()
    self.__print_board_be()

  __row_col = [(9,9), (16,16), (16,30)]
  __mines   = [10, 40, 99]
  __cells   = [m*n for m,n in __row_col]

  def __init_board(self):
    n, m = MinesGame.__row_col[self.__level]
    self.__board_be = [[0]*m for k in range(n)]

  def __get_x_y(self, num):
    n, m = MinesGame.__row_col[self.__level]
    return (num//m, num % m)

  def __set_mines(self):
    mines = MinesGame.__mines[self.__level]
    nums  = MinesGame.__cells[self.__level]
    cells = list(x for x in range(nums))
    for n in range(mines):
      k = randint(0, len(cells)-n)
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
    for row in self.__board_be: print(row)

game = MinesGame()
