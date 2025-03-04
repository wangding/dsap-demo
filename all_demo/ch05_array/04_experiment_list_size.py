#!/usr/bin/env python

# 检查 list 的扩容策略
data = []
for k in range(100):
  print(f'数组长度: {len(data):2d};',
        f'数组字节数: {data.__sizeof__():3d}')
  data.append(None)
