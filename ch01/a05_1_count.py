# 计算列表中给定目标出现次数的函数
 
def count(data, target):
  n = 0
  for item in data:
    if item == target:
      n += 1
  return n

print(count([29, 13, 'cron', 13], 13))
print(count([29, 13, 'cron', 13], 'cron'))
print(count([29, 13, 'cron', 13], 'gold'))
