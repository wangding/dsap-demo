s = 'hello, world'

print(s)
print('len(s) =', len(s))
print('s[-1] =', s[-1])
print('s[11] =', s[11])
print()

for k in range(-1, -len(s)-1, -1):
  j = len(s) + k
  print(f's[{k}] = {s[k]}', end="  |  ")
  print(f's[{j}] = {s[j]}')