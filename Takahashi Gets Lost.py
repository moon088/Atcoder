# C
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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

H,W,N=MAP()
T=input()
board = BOARD(H)
cnt=0

U=[None for _ in range(N)]
for i in range(N):
    if T[i]=="L":
        U[i]=Dxy[3]
    elif T[i]=="R":
        U[i]=Dxy[2]
    elif T[i]=="U":
        U[i]=Dxy[1]
    else:
        U[i]=Dxy[0]

for i in range(H-1):
    for j in range(W-1):
        if board[i][j]=="#":
            continue
        x=j
        y=i
        for k in range(N):
            x+=U[k][1]
            y+=U[k][0]
            
            if 0<= y < H and 0 <= x < W and board[y][x]==".":
                continue
            else:
                break
        else:
            cnt+=1
        
print(cnt)