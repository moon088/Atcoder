"""
問題:
https://qiita.com/Ll_e_ki/items/fa475f5bb224ada9be97

以下の二つを満たす経路のうち、通った辺の重みの総和が最小のものを求めよ。経路が存在しない場合は-1を出力
・ある頂点から出発し、最後には戻ってくる経路である
・すべての頂点をちょうど1回通る経路である
V E
s0 t0 d0
s1 t1 d1
:
sE-1 tE-1 dE-1
となっており、Vは頂点の数、Eは辺の数
si, ti, diは頂点siから頂点tiに向かって重みがdiの辺が張られている

"""

import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
from cmath import phase
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from functools import cmp_to_key
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush , heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


V, E = MAP()
cost = [[INF]*V for i in range(V)] #初期値INF
for i in range(E):
    s,t,d = MAP()
    cost[s][t] = d     #idnexは調整する
dp = [[INF]*V for i in range(2**V)] # dpの長さは2^V必要
dp[0][0] = 0  #start


for S in range(2**V): # Sは集合をbitで表している
    for v in range(V): # vは配られる側
        for u in range(V): # uは配る側
            if not (S >> u) & 1 and S != 0: #u番目の頂点に訪れていない
                continue
            if (S >> v) & 1 == 0: #v番目にすでに訪れたなら通れない
                if dp[S][u] + cost[u][v] < dp[S | (1 << v)][v]:
                    dp[S | (1 << v)][v] = dp[S][u] + cost[u][v] #|はor演算

# 全ての要素が含まれていて、末項が0のものの最小コストを出力する
# infだった場合は到達できないということなので-1を出力する
if dp[2**V-1][0] != INF:
    print(dp[2**V-1][0])
else:
    print(-1)
