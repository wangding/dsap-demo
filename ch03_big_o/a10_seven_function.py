#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# 定义x轴的范围
n = np.arange(1, 21)  # 从1到20，避免log(0)未定义

# 定义各个量级函数
constant = np.ones_like(n)  # O(1)
logarithmic = np.log2(n)    # O(log n)
linear = n                  # O(n)
linearithmic = n * np.log2(n)  # O(n log n)
quadratic = n**2            # O(n^2)
polynomial = n**3           # O(n^3)
exponential = 5**n          # O(5^n)

# 创建图表
plt.figure(figsize=(10, 6))

# 绘制各个函数
plt.plot(n, constant, label='O(1)', linestyle='-', color='blue')
plt.plot(n, logarithmic, label='O(log n)', linestyle='--', color='green')
plt.plot(n, linear, label='O(n)', linestyle='-.', color='red')
plt.plot(n, linearithmic, label='O(n log n)', linestyle=':', color='orange')
plt.plot(n, quadratic, label='O(n^2)', linestyle='-', color='purple')
plt.plot(n, polynomial, label='O(n^3)', linestyle='--', color='brown')
plt.plot(n, exponential, label='O(5^n)', linestyle='-.', color='black')

# 设置图表标题和标签
plt.title('Comparison of Time Complexity Functions')
plt.xlabel('Input Size (n)')
plt.ylabel('Operations')

# 设置网格
plt.grid(True)

# 设置对数刻度（y轴），以便更好地显示不同数量级的函数
plt.yscale('log')
plt.ylim(1, 1e6)  # 设置y轴的范围，以适应所有函数

# 添加图例
plt.legend()

# 显示图表
plt.show()
