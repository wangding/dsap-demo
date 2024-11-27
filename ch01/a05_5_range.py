# 函数的默认参数
# 函数默认参数交换位置的小技巧

def range(start, stop=None, step=1):
  if stop is None:
    stop = start
    start = 0
    
  while start < stop:
    print(start, end=' ')
    start += step
  print()

# start = 5 => start = 0, stop = 5
range(5)       # 0 1 2 3 4

range(1, 5)    # 1 2 3 4
range(1, 5, 2) # 1 3