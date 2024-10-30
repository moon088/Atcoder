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


def is_bipartite(N, G):
    color = [-1] * N  # 各頂点の色 (-1: 未着色, 0: 色1, 1: 色2)
    for v in range(N):
        if color[v] != -1:  
            continue
        que = deque([v])
        color[v] = 0
        while que:
            v = que.popleft()
            for nv in G[v]:
                if color[nv] == -1:
                    color[nv] = 1 - color[v]  # 隣接頂点と異なる色で塗る
                    que.append(nv)
                elif color[nv] == color[v]: 
                    return False
    return True


N,M=MAP()
A=LIST()
B=LIST()
board = [[] for _ in range(N)]
for i in range(M):
    a = A[i]-1
    b = B[i]-1
    board[a].append(b)
    board[b].append(a)

if is_bipartite(N, board):
    print("Yes")
else:
    print("No")
