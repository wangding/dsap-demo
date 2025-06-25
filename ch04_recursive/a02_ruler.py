#!/usr/bin/env python

# 递归绘制英制标尺

def draw_line(tick_length, tick_label=''):
  line = '-' * tick_length
  if tick_label:
    line += ' ' + tick_label
  print(line)

def draw_interval(center_length):
  if center_length > 0:
    draw_interval(center_length - 1)
    draw_line(center_length)
    draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
  draw_line(major_length, '0')
  for j in range(1, 1 + num_inches):
    draw_interval(major_length - 1)
    draw_line(major_length, str(j))


if __name__ == '__main__':
  draw_ruler(2, 4)
  print('='*30)
  draw_ruler(1, 5)
  print('='*30)
  draw_ruler(3, 3)
