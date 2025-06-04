class Graph:
  def __init__(self, edges=None, directed=False):
    self.__V = {}         # 顶点集合，字典形式，key为顶点，value为顶点索引
    self.__A = []         # 邻接矩阵
    self.__n = len(edges) # 边数
    self.__build_graph(edges, directed)

  def __repr__(self):     return '\n'.join(' '.join(str(c) for c in row) for row in self.__A)
  def vertex_count(self): return len(self.__V)
  def vertices(self):     return self.__V.keys()
  def edges(self):        return [(u, v, self.__A[self.__V[u]][self.__V[v]]) for u in self.__V for v in self.__V if self.__A[self.__V[u]][self.__V[v]] != 0]
  def edge_count(self):   return self.__n
  def get_edge(self, u, v):
    if u not in self.__V or v not in self.__V: return None
    return self.__A[self.__V[u]][self.__V[v]]
  def degree(self, u):
    if u not in self.__V: return None
    index = self.__V[u]
    return sum(1 for v in self.__A[index] if v != 0)
  
  def __build_graph(self, edges, directed):
    if edges is None: return
    index = 0
    for u, v, w in edges:
      if u not in self.__V: self.__V[u] = index; index += 1
      if v not in self.__V: self.__V[v] = index; index += 1

    m = len(self.__V)
    self.__A = [[0] * m for _ in range(m)]

    for u, v, w in edges:
      i = self.__V[u]
      j = self.__V[v]
      self.__A[i][j] = w
      if not directed: self.__A[j][i] = w

if __name__ == "__main__":
  edges = [
    ('u', 'v', 'e'),
    ('w', 'v', 'f'),
    ('z', 'w', 'h'),
    ('u', 'w', 'g'),
  ]
  g = Graph(edges)
  print(g)
  print("顶点数:", g.vertex_count())
  print("顶点:", g.vertices())
  print("边数:", g.edge_count())
  print("边:", g.edges())
  print("u-v的边:", g.get_edge('u', 'v'))
  print("u的度数:", g.degree('u'))