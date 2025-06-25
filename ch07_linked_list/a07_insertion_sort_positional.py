#!/usr/bin/env python

def insertion_sort(L):

  if len(L) > 1:
    marker = L.first()
    while marker != L.last():
      pivot = L.after(marker)
      value = pivot.element()
      if value > marker.element():
        marker = pivot
      else:
        walk = marker
        while walk != L.first() and L.before(walk).element() > value:
          walk = L.before(walk)
        L.delete(pivot)
        L.add_before(walk, value)
