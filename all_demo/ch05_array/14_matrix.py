#!/usr/bin/env python

# 矩阵运算
def add(m1, m2):
  # v1
  # n, m = len(m1), len(m1[0])
  # m3 = [[0]*m for j in range(n)]
  # for x in range(n):
  #   for y in range(m):
  #     m3[x][y] = m1[x][y] + m2[x][y]
  # return m3

  # v2
  # return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))]
  #                              for i in range(len(m1))]
  
  # v3
  return [[x+y for x,y in zip(r1, r2)]
               for r1, r2 in zip(m1, m2)]

def multiply(m1, m2):
  # v1
  # n, m = len(m1), len(m2[0])
  # m3 = [[0]*m for j in range(n)]
  # for x in range(n):
  #   for y in range(m):
  #     a = m1[x]
  #     b = [row[y] for row in m2]
  #     m3[x][y] = sum([a[i]*b[i] for i in range(len(a))])
  # return m3
  
  # v2
  return [[sum(a * b for a, b in zip(row, col)) 
            for col in zip(*m2)] 
            for row in m1]
m1 = [
  [1, 2, 3],
  [4, 5, 6]
]

m2 = [
  [4, 5, 6],
  [7, 8, 9]
]

m3 = [
  [4, 5],
  [6, 7],
  [8, 9]
]

print(add(m1, m2))
print(multiply(m1, m3))