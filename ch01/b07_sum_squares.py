def sum_squares(n):
  return sum([x**2 for x in range(n+1) if x%2 == 1])

print('1~5 sum of the squares:', sum_squares(5))