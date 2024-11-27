# 没有显示检查，代码会自己抛出异常

def sum(values):
  total = 0
  for v in values:
    total = total + v
  return total

print(sum([1, 2, 3]))
print(sum((1, 2, 3)))

# TypeError: 'int' object is not iterable
# print(sum(4))

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(sum(['a', 'b']))