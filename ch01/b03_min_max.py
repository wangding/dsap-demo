def min_max(arr):
  min = max = arr[0]
  for x in arr:
    if x < min:
      min = x
    if x > max:
      max = x
  return min, max

min, max = min_max([1, 5, 3, 2, 4])

print('1, 5, 3, 2, 4')
print(f'min = {min}')
print(f'max = {max}')