import io
import sys

_INPUT = """\
6
6 7
1 2
1 4
1 5
2 4
2 3
3 5
3 6
8 7
7 8
3 4
5 6
5 7
5 8
6 7
6 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  class UnionFind():
    def __init__(self, n):
      self.n = n
      self.parents = [-1] * n
    def find(self, x):
      if self.parents[x] < 0:
        return x
      else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.parents[x] > self.parents[y]:
        x, y = y, x
      self.parents[x] += self.parents[y]
      self.parents[y] = x
    def size(self, x):
      return -self.parents[self.find(x)]
    def same(self, x, y):
      return self.find(x) == self.find(y)
    def members(self, x):
      root = self.find(x)
      return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
      return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
      return len(self.roots())
    def all_group_members(self):
      return {r: self.members(r) for r in self.roots()}
    def __str__(self):
      return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  for i in range(M):
    A,B=map(int,input().split())
    A-=1; B-=1
    G[A].append(B)
  uf=UnionFind(N)
  ans=[]
  tmp=0
  for i in reversed(range(1,N)):
    tmp+=1
    for v in G[i]:
      if uf.find(i)!=uf.find(v):
        tmp-=1
        uf.union(i,v)
    ans.append(tmp)
  ans=ans[::-1]
  for i in range(N-1):
    print(ans[i])
  print(0)