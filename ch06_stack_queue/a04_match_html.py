#!/usr/bin/env python

# 用栈进行 HTML 标记匹配检测

from a01_array_stack import ArrayStack

def is_matched_html(raw):
  S = ArrayStack()
  j = raw.find('<')
  while j != -1:
    k = raw.find('>', j+1)
    if k == -1:
      return False
    tag = raw[j+1:k]
    if not tag.startswith('/'):
      S.push(tag)                 
    else:
      if S.is_empty():
        return False
      if tag[1:] != S.pop():   
        return False
    j = raw.find('<', k+1)
  return S.is_empty()

if __name__ == '__main__':
  html = '<html><head></head><body>hello</body></html>'
  print(is_matched_html(html))