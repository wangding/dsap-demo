# Python 中所有标识符都是对象

age = 20
name = 'wangding'

def add(x, y):
  return x + y

class Student: pass

# 所有标识符都是对象，而对象是类的实例
print(age.__class__)
print(name.__class__)
print(add.__class__)
print(Student.__class__)
print()

# 所有类的基类是 <class 'object'>
print(age.__class__.__base__)
print(name.__class__.__base__)
print(add.__class__.__base__)
print(Student.__base__)