# 抛出异常

from collections.abc import Iterable

def sum(values):
  if not isinstance(values, Iterable):
    raise TypeError('parameter must be an iterable type')
  total = 0
  for v in values:
    if not isinstance(v, (int, float)):
      raise TypeError('elements must be numeric')
    total = total+ v
  return total

print(sum([1, 2, 3]))
print(sum((1, 2, 3)))

# TypeError: parameter must be an iterable type
# print(sum(4))

# TypeError: elements must be numeric
# print(sum(['a', 'b']))
