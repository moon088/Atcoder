# E
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

H,W=MAP()
S=BOARD(H)

class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n #-5なら要素5こ持つ根

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

red_cnt=0
uf = UnionFind(H*W)
#node num: i*H+W
for i in range(H):
    for j in range(W):
        if S[i][j]==".":
            red_cnt+=1
        for dx, dy in Dxy:
            if 0<= i+dy < H and 0<= j+dx<W:
                if S[i][j]==S[i+dy][j+dx]=="#" and not uf.same(i*W+j,(i+dy)*W+dx+j):
                    uf.union(i*W+j, (i+dy)*W+dx+j)
#print(uf.__dict__)
##print(uf.group_count())
#print(red_cnt)

MOD = 998244353 
ans=0
renketu = uf.group_count() - red_cnt
for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            continue
        
        l = set()
        for dx, dy in Dxy:
            if 0<= i+dy < H and 0<= j+dx<W and S[i+dy][j+dx]=="#":
                l.add(uf.find((i+dy)*W+dx+j))
        heru = len(l)-1
        #print(heru)
        ans += renketu-heru
        ans%=MOD


print(ans * pow(red_cnt,-1,MOD) % MOD)


