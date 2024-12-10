def sum_squares(n):
  total = 0
  for i in range(n+1):
    if i%2 == 1:
      total += i**2
  return total

print('1~5 sum of the squares:', sum_squares(5))