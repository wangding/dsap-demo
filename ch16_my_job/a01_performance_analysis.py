# 从大到小在列表中放十万个连续的整数
# 不同方案的性能对比，请思考背后原因

from time import time

N = 10**6
def report(data, cost):
  print(data[:2] + ['...'] + [data[-1]], \
        f'use {cost:.5} s')

# 方案一：列表尾部顺序放入，然后逆序
start = time()
data = []
for val in range(N):
  data.append(val)
data.reverse()
end = time()
report(data, end-start)

# 方案二：列表头部逆序放入
start = time()
data = []
for val in range(N):
  data.insert(0, val)
end = time()
report(data, end-start)

# 方案三：列表导出式
start = time()
data = [x for x in range(N-1, -1, -1)]
end = time()
report(data, end-start)
