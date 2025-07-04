#!/usr/bin/env python

# 基于数组的最高分榜单应用

class GameEntry:
  def __init__(self, name, score):
    self._name = name
    self._score = score

  def get_name(self):
    return self._name
    
  def get_score(self):
    return self._score

  def __str__(self):
    return f'({self._name}, {self._score})'

class Scoreboard:
  def __init__(self, capacity=10):
    self._board = [None] * capacity
    self._n = 0

  def __getitem__(self, k):
    return self._board[k]

  def __str__(self):
    return '\n'.join(str(self._board[j]) for j in range(self._n))

  def add(self, entry):
    score = entry.get_score()

    good = self._n < len(self._board) or \
           score > self._board[-1].get_score()

    if good:
      if self._n < len(self._board):
        self._n += 1

      j = self._n - 1
      while j > 0 and self._board[j-1].get_score() < score:
        self._board[j] = self._board[j-1]
        j -= 1
      self._board[j] = entry

if __name__ == '__main__':
  board = Scoreboard(5)
  for e in (
    ('Rob', 750), ('Mike',1105), ('Rose', 590), ('Jill', 740),
    ('Jack', 510), ('Anna', 660), ('Paul', 720), ('Bob', 400),
    ):
    ge = GameEntry(e[0], e[1])
    board.add(ge)
    print(f'After considering {ge}, scoreboard is:')
    print(board)
    print()
