# D
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
from cmath import phase
from itertools import accumulate, chain, combinations, combinations_with_replacement, permutations, compress, dropwhile, takewhile, groupby, product, starmap
from functools import cmp_to_key
from operator import itemgetter, mul, xor
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush , heappop
from functools import reduce, lru_cache
#it is code to make recursion a bit faster
#Pimport pypyjit
#pypyjit.set_param("max_unroll_recursion=-1")
#recursion limit
#sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def list_input(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def LIST_3D(n): return [[LIST() for _ in range(n)] for _ in range(n)] #Axyz is (y*z)*x
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return map(list, zip(*(map(int, input().split()) for _ in range(n))))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def BOARD_INT(H): return [list(map(int, input().split())) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N,M=MAP()
board = [[] for _ in range(N)]
for i in range(M):
    a,b,x,y=MAP()
    a-=1
    b-=1
    board[a].append((a,b,x,y))
    board[b].append((b,a,-x,-y))


class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n #-5なら要素5こ持つ根
    self.zahyou = [[None, None] for _ in range(n)]

#要素x が属するグループの根を返す
  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  #xとyが属するグループの併合
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x
    

  #グループのサイズ返す
  def size(self, x):
      return -self.parents[self.find(x)]

  #xとyが同じグループに属するかどうか
  def same(self, x, y):
    return self.find(x) == self.find(y)

  #xが属するグループのリスト
  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  #すべての根のリスト
  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

  #グループ数
  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    group_members = defaultdict(list)
    for member in range(self.n):
      group_members[self.find(member)].append(member)
    return group_members

  #printでの表示用
  def __str__(self):
    return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

  def make(self, a,b,x,y):
      if self.zahyou[a][0]==None:
          self.zahyou[a][0] = self.zahyou[b][0]+X
          self.zahyou[a][1] = self.zahyou[b][1]+y
      else:
          self.zahyou[b][0] = self.zahyou[a][0]+x
          self.zahyou[b][1] = self.zahyou[a][1]+y


uf = UnionFind(N)
uf.zahyou[0][0] = 0
uf.zahyou[0][1] = 0

q = deque(board[0])
#print(q)
while q:
    a, b, x, y = q.pop()
    if not uf.same(a,b):
        if uf.same(0,a) and not uf.same(0,b):
            uf.union(a, b)
            uf.make(a,b,x,y)
            q+=board[b]

for i in range(N):
    zahyou = uf.zahyou[i]
    if zahyou[0]==None:
        print("undecidable")
    else:
        print(*zahyou)