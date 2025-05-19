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


N,M=MAP()
U,V,T=ZIP(M)
g = [[INF]*N for _ in range(N)]
for i in range(M):
    u,v,t=U[i]-1,V[i]-1,T[i]
    g[u][v]=min(g[u][v], t)
    g[v][u]=min(g[v][u], t)
for i in range(N):
    g[i][i]=0
    
    
def warshall_floyd(n, dist):
    new_dist = [row[:] for row in dist]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                new_dist[i][j] = min(new_dist[i][j], new_dist[i][k] + new_dist[k][j])

    return new_dist

warshall = warshall_floyd(N, g)
Q=INT()
for i in range(Q):
    K=INT()
    B=LIST()
    ans=INF
    for bits in range(1<<K):
        for per in permutations(range(K),K):
            temp = 0
            now = 0
            for j in range(K):
                #print(temp, now)
                usefrom, useto, usecost = U[B[per[j]]-1]-1, V[B[per[j]]-1]-1, T[B[per[j]]-1]
                if (bits>>j)&1:
                    temp += warshall[now][usefrom]+usecost
                    now = useto
                else:
                    temp += warshall[now][useto]+usecost
                    now = usefrom
                #print(temp, now)
            temp += warshall[now][N-1]
            ans = min(ans, temp)
    print(ans)
                    