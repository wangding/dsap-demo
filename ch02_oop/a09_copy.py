#!/usr/bin/env python

# 浅拷贝 vs 深拷贝

# 列表元素共享引用，x0 中元素相同
x0 = [{0}] * 3
for i in range(3): print(f'x0[{i}] id:', id(x0[i]), x0[i])

print('-----x0[0].add(1)-----')
x0[0].add(1)
for i in range(3): print(f'x0[{i}] id:', id(x0[i]), x0[i])
print()

# 列表元素没有共享引用，x1 中元素不同
x1 = [{1}, {2}, {3}]
for i in range(3): print(f'x1[{i}] id:', id(x1[i]), x1[i])
print()

# 列表对象共享引用, x2 is x1
x2 = x1
print('x1 id:', id(x1))
print('x2 id:', id(x2))
for i in range(3): print(f'x2[{i}] id:', id(x2[i]), x2[i])
print()

# 列表对象浅拷贝, x3 is not x1
# 但元素存在共享, elm in x3 is elm in x1
x3 = list(x1)
print('x1 id:', id(x1))
print('x3 id:', id(x3))
for i in range(3): print(f'x3[{i}] id:', id(x3[i]), x3[i])
print()

# 列表对象深拷贝, x4 is not x1
# 且元素没有共享, elm in x4 is not elm in x1
import copy
x4 = copy.deepcopy(x1)
print('x1 id:', id(x1))
print('x4 id:', id(x4))
for i in range(3): print(f'x4[{i}] id:', id(x4[i]), x4[i])