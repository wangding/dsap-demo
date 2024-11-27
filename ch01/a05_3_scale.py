# 函数的可变参数

def scale(data, factor):
  for j in range(len(data)):
    data[j] *= factor

arr = [1, 2, 3]
print('start:', arr)

scale(arr, 3)
print('end:  ', arr)