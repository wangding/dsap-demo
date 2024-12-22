#!/usr/bin/env python

from a08_favorites_list import FavoritesList
from a06_positional_list import PositionalList

class FavoritesListMTF(FavoritesList):
  def _move_up(self, p):               
    if p != self._data.first():
      self._data.add_first(self._data.delete(p))

  def top(self, k):
    if not 1 <= k <= len(self):
      raise ValueError('Illegal value for k')

    temp = PositionalList()
    for item in self._data:
      temp.add_last(item)

    for j in range(k):
      highPos = temp.first()
      walk = temp.after(highPos)
      while walk is not None:
        if walk.element()._count > highPos.element()._count:
          highPos = walk
        walk = temp.after(walk)
      yield highPos.element()._value
      temp.delete(highPos)

if __name__ == '__main__':
  fav = FavoritesListMTF()
  for c in 'hello. this is a test of mtf':
    fav.access(c)
    k = min(5, len(fav))
    print('Top {0}) {1:25} {2}'.format(k, [x for x in fav.top(k)], fav))
