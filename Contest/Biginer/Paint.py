#E
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


H,W,M=MAP()
T,A,X=ZIP(M)
row=[False for _ in range(H)]+[0]
col = [False for _ in range(W)]+[0]
d=defaultdict(int)

zero=H*W
for i in range(M-1,-1,-1):
    if T[i]==1:
        if not row[A[i]-1]:
            d[X[i]] += W - col[-1]
            row[A[i]-1]=True
            row[-1]+=1
            zero-=W-col[-1]
    else:
        if not col[A[i]-1]:
            d[X[i]] += H - row[-1]
            col[A[i]-1] = True
            col[-1]+=1
            zero-=H-row[-1]
    #print(d,row,col)
d[0]+=zero
#print(d)
d_sorted = dict(sorted(d.items()))
d_sorted = {k:v for k,v in d_sorted.items() if v!=0}

print(len(d_sorted))
for i in d_sorted:
    print(i,d_sorted[i])
