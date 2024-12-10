import random as rnd

arr = [1, 3, 5, 7, 9]
print(rnd.choice(arr))
print(rnd.randrange(len(arr)))

def choice(arr):
  return arr[rnd.randrange(len(arr))]

print(choice(arr))