#!/usr/bin/env python

# 递归查看磁盘占用

import os
from pathlib import PurePath

def disk_usage(path):
  total = os.path.getsize(path)
  if os.path.isdir(path):
    for filename in os.listdir(path):
      childpath = os.path.join(path, filename)
      total += disk_usage(childpath)

  print ('{0:<7}'.format(total), path)
  return total

if __name__ == '__main__':
  path = PurePath(os.path.dirname(__file__)).parent
  print(disk_usage(path))
