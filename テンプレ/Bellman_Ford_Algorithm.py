"""
問題:
https://atcoder.jp/contests/abc061/tasks/abc061_d
頂点1からNまでのスコアの最大値を求める。ただしいくらでも大きくなる場合はinfを出力する

入力:
6 5 #N M(Nは頂点数)
1 2 -1000000000 #頂点1->2の重みが-10000000
2 3 -1000000000
3 4 -1000000000
4 5 -1000000000
5 6 -1000000000
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

N,M = MAP()
edge=[]
for i in range(M):
    a,b,c,=MAP()
    edge.append((a,b,c))

#今回はmax
def bellman_ford_max_score(N, edges):
    #初期化
    distance = [-INF] * (N + 1)
    distance[1] = 0  
    
    #リラクゼーション
    for _ in range(N - 1): #頂点数-1回まわすのがポイント
        for u, v, w in edges:
            if distance[u] != -INF and distance[u] + w > distance[v]:
                distance[v] = distance[u] + w
                
    #負の閉路の検出
    for _ in range(N - 1):
        updated = False
        for u, v, w in edges:
            if distance[u] != -INF and distance[u] + w > distance[v]:
                distance[v] = INF
                updated = True
        if not updated:
            break

    #出力
    if distance[N] == INF:
        print("inf")
    else:
        print(distance[N])

bellman_ford_max_score(N,edge)