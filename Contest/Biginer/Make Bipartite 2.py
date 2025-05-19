<<<<<<< HEAD
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
from sortedcontainers import SortedSet, SortedList, SortedDict
#it is code to make recursion a bit faster
#Pimport pypyjit
#pypyjit.set_param("max_unroll_recursion=-1")
#recursion limit
sys.setrecursionlimit(10**7)
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
def isInBoard(H,W,y,x): return 0<=y<H and 0<=x<W
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60



class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n #-5なら要素5こ持つ根
    self.node = [0]*n

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
      self.node[x]+=1
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.node[x] += self.node[y] +1
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


def is_bipartite(N, G):
    color = [-1] * N 
    group = []
    for v in range(N):
        if color[v] != -1:  
            continue
        que = deque([v])
        color[v] = 0
        temp = [[], 0]
        while que:
            v = que.popleft()
            temp[0].append(v)
            for nv in G[v]:
                if color[nv] == -1:
                    color[nv] = 1 - color[v] 
                    que.append(nv)
                    if color[nv]==1:
                        temp[1]+=1
                elif color[nv] == color[v]: 
                    return False,color
        group.append(temp)
    return True,group

N,M=MAP()
g=[[] for _ in range(N)]
uf = UnionFind(N)
for i in range(M):
    u,v=MAP(); u-=1; v-=1
    g[u].append(v); g[v].append(u)
    uf.union(u,v)
f, group = is_bipartite(N,g)


ans = 0
now=0
if f:
    for x in group:
        s = len(x[0])
        temp = x[1]*(s-x[1])-uf.node[uf.find(x[0][0])]
        ans += temp
        ans += now*s
        now += s

    print(ans)
else:
=======
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
from sortedcontainers import SortedSet, SortedList, SortedDict
#it is code to make recursion a bit faster
#Pimport pypyjit
#pypyjit.set_param("max_unroll_recursion=-1")
#recursion limit
sys.setrecursionlimit(10**7)
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
def isInBoard(H,W,y,x): return 0<=y<H and 0<=x<W
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60



class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n #-5なら要素5こ持つ根
    self.node = [0]*n

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
      self.node[x]+=1
      return

    if self.parents[x] > self.parents[y]:
      x, y = y, x

    self.node[x] += self.node[y] +1
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


def is_bipartite(N, G):
    color = [-1] * N 
    group = []
    for v in range(N):
        if color[v] != -1:  
            continue
        que = deque([v])
        color[v] = 0
        temp = [[], 0]
        while que:
            v = que.popleft()
            temp[0].append(v)
            for nv in G[v]:
                if color[nv] == -1:
                    color[nv] = 1 - color[v] 
                    que.append(nv)
                    if color[nv]==1:
                        temp[1]+=1
                elif color[nv] == color[v]: 
                    return False,color
        group.append(temp)
    return True,group

N,M=MAP()
g=[[] for _ in range(N)]
uf = UnionFind(N)
for i in range(M):
    u,v=MAP(); u-=1; v-=1
    g[u].append(v); g[v].append(u)
    uf.union(u,v)
f, group = is_bipartite(N,g)


ans = 0
now=0
if f:
    for x in group:
        s = len(x[0])
        temp = x[1]*(s-x[1])-uf.node[uf.find(x[0][0])]
        ans += temp
        ans += now*s
        now += s

    print(ans)
else:
>>>>>>> 5a60e3f (Sync local Atcoder directory)
    print(0)