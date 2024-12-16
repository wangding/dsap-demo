#!/usr/bin/env python

# 根据成绩等级列表 grades，计算平均绩点的函数
# 函数的可选参数 points

def compute_gpa(
      grades, 
      points={'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33,
              'B':3.0, 'B-':2.67,'C+':2.33, 'C':2.0,
              'C':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}
      ):
  num_courses = 0
  total_points = 0
  for g in grades:
    if g in points:
      num_courses += 1
      total_points += points[g]
  return total_points / num_courses

print(compute_gpa(['A-', 'A-', 'A-']))
