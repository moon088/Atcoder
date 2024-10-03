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
 


"""N,M=MAP()
deg = [0]*N
dis = [0]*N
graph = [[] for _ in range(N)]
for i in range(M):
    u,v,w=MAP()
    graph[u-1].append([v-1,w])
    graph[v-1].append([u-1,-w])
    deg[v-1]+=1

visited=[False]*N
for temp in range(N):
    if visited[temp]:
        continue
    #BFS
    bfs_q = deque([temp])

    while bfs_q:
        now = bfs_q.popleft()
        visited[now]=True
        for i in range(len(graph[now])):
            near = graph[now][i]
            if visited[near[0]]:
                continue
            visited[near[0]]=True
            dis[near[0]] = dis[now] + near[1]
            bfs_q.append(near[0])        
print(*dis)
"""


class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * (n)
        # 根への距離
        self.weight = [0] * (n)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            # 親への重みを追加しながら根まで走査
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        # 木の高さ考慮して併合
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            #　高さ同じ
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # xからyへのコスト
    def diff(self, x, y):
        return self.weight[x] - self.weight[y]
    
N,M=MAP()
uf = WeightedUnionFind(N)
for i in range(M):
    u,v,w=MAP()
    u-=1
    v-=1
    uf.union(u, v, w)

group = dict()

for i in range(N):
    p = uf.find(i)
    if p not in group:
        group[p] = []
    group[p].append([i, uf.weight[i]])

ans = [0] * N
for key, values in group.items():
    diff = 0
    val = [v_i for _, v_i in values]
    if min(val) < - 10 ** 18:
        diff = - 10 ** 18 + min(val)
    elif max(val) > 10 ** 18:
        diff = 10 ** 18 - max(val)
    for i, v_i in values:
        ans[i] = v_i + diff

for i in ans:
    print(-i,end=" ")