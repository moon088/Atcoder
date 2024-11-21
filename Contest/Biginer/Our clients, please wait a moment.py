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

N,A,B,C=MAP()
board = BOARD_INT(N)
cost = [[INF, INF] for _ in range(N)]
cost[0][0]=0

hq = [(0,0,0)] #cost, flag, toV
while hq:
    d, flag, v = heappop(hq)
    if cost[v][flag]<d:
        continue
    for nv in range(N):
        if flag:
            near_cost = cost[v][1] + board[v][nv]*B+C
            if near_cost<cost[nv][1]:
                cost[nv][1]=near_cost
                heappush(hq, (near_cost, 1, nv)) 
        else:   
            near_cost_0 = cost[v][0] + board[v][nv]*A
            if near_cost_0<cost[nv][0]:
                cost[nv][0]=near_cost_0
                heappush(hq, (near_cost_0, 0, nv))
            near_cost_1 = cost[v][0] + board[v][nv]*B+C
            if near_cost_1<cost[nv][1]:
                cost[nv][1]=near_cost_1
                heappush(hq, (near_cost_1,1,nv))
print(min(cost[N-1][0], cost[N-1][1]))   