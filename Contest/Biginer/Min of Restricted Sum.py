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


N, M = MAP()
g = [[] for _ in range(N)]
for _ in range(M):
    x, y, z = MAP(); x-=1; y-=1
    if x == y:
        if z != 0:
            print(-1)
            exit()
        continue
    g[x].append((y, z)); g[y].append((x, z))

A = [0] * N; d = [0] * N      
visited = [False] * N

for i in range(N):
    if visited[i]: continue
    group = []  
    q = deque()
    q.append(i)
    visited[i] = True
    d[i] = 0  

    while q:
        now = q.popleft()
        group.append(now)
        for near, w in g[now]:
            if not visited[near]:
                visited[near] = True
                d[near] = d[now] ^ w
                q.append(near)
            else:
                if d[near] != d[now] ^ w:
                    print(-1)
                    exit()
    r = 0
    gsize = len(group)
    for bit in range(32):
        one = 0
        for v in group:
            if (d[v] >> bit) & 1:
                one += 1
        if one > gsize - one:
            r |= (1 << bit)
    for v in group:
        A[v] = r ^ d[v]

print(*A)



N,M=MAP()
X,Y,Z=ZIP(M)

