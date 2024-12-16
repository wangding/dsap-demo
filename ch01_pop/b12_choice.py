#!/usr/bin/env python

import random as rnd

data = [1, 3, 5, 7, 9]
print(rnd.choice(data))
print(rnd.randrange(len(data)))

def choice(data):
  return data[rnd.randrange(len(data))]

print(choice(data))