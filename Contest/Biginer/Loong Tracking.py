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
def list_input(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]#R,L,U,D
INF = 1 << 60

N,Q=MAP()
route= [(1,0)]
ans=[]
for i in range(Q):
    flag, s = input().split()
    if int(flag)==1:
        now=route[-1]
        if s == "R":
            x,y=now[0]+Dxy[0][0], now[1]+Dxy[0][1]
        elif s == "L":
            x,y=now[0]+Dxy[1][0], now[1]+Dxy[1][1]
        elif s == "U":
            x,y=now[0]+Dxy[2][0], now[1]+Dxy[2][1]
        else:
            x,y=now[0]+Dxy[3][0], now[1]+Dxy[3][1]
        route.append((x,y))
    else:
        s = int(s)
        #print(route)
        if s<=len(route):
            zahyou = route[-s]
            ans.append((zahyou[0], zahyou[1]))
        else:
            idx = s-len(route) +1
            ans.append((idx,0))
for i in ans:
    print(i[0], i[1])