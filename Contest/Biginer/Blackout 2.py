# E
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd, prod
from cmath import phase
from itertools import accumulate, chain, combinations, combinations_with_replacement, permutations, compress, dropwhile, takewhile, groupby, product, starmap
from functools import cmp_to_key,lru_cache
from operator import itemgetter, mul, xor
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush , heappop
from functools import reduce, lru_cache
from sortedcontainers import SortedSet, SortedList, SortedDict
from decimal import Decimal, ROUND_HALF_UP
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
def ROUND_OFF(X,k): return  (X // (10 ** k) + 5) // 10 * 10 ** (k + 1)
def YES(): return print("Yes")
def NO(): return print("No")
alph = 'abcdefghijklmnopqrstuvwxyz'
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60



class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] *n #-5なら要素5こ持つ根
    self.denki = [False]*n

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
    if  self.denki[y]:
      self.denki[x]=True

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

  def denkion(self, x):
    parent = self.find(x)
    self.denki[parent] = True
  

N, M, E=MAP()
U, V=ZIP(E)
Q=INT()
X=[]; s = set()
for i in range(Q):
    x=INT()
    X.append(x-1)
    s.add(x-1)

uf = UnionFind(N)
for i in range(E):
    if i in s: continue
    u, v = U[i]-1, V[i]-1
    if u>=N and v>=N: continue
    if u>=N:
      uf.denki[uf.find(v)]=True
    elif v>=N:
      uf.denki[uf.find(u)]=True
    else:
      uf.union(u,v)
    
now=0
for i in range(N):
  parent = uf.find(i)
  if uf.denki[parent]:
    now+=1


ans = [now]
for i in range(Q):
    x = X[Q-i-1]
    u,v = U[x]-1, V[x]-1
    if u>=N and v>=N: 
      ans.append(ans[-1])
    else:
      if u>=N:
        pv = uf.find(v)
        if not uf.denki[pv]:
          ans.append(ans[-1]+uf.size(pv))
          uf.denki[pv]=True
        else:
          ans.append(ans[-1])
      elif v>=N:
        pu = uf.find(u)
        if not uf.denki[pu]:
          ans.append(ans[-1]+uf.size(pu))
          uf.denki[pu]=True
        else:
          ans.append(ans[-1])
      else:
        pu = uf.find(u); pv = uf.find(v)
        if uf.denki[pu] and uf.denki[pv]:
          ans.append(ans[-1])
        elif uf.denki[pu]:
          ans.append(ans[-1]+uf.size(pv))
        elif uf.denki[pv]:
          ans.append(ans[-1]+uf.size(pu))
        else:
          ans.append(ans[-1])
        uf.union(u, v)
    #print(ans, uf.all_group_members(), uf.denki)

for i in range(Q):
    print(ans[len(ans)-2-i])
    


