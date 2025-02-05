# D
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

H,W,sy,sx = MAP()
dcol = defaultdict(SortedSet)
drow = defaultdict(SortedSet)

N=INT()
for i in range(N):
    r,c=MAP()
    dcol[c].add(r); drow[r].add(c)
    dcol[c].update([0,H+1]); drow[r].update([0,W+1])
d = {"U":Dxy[1], "D":Dxy[0], "R":Dxy[2], "L":Dxy[3]}

Q=INT()
for i in range(Q):
    d,l=input().split(); l = int(l)
    if d=="U":
        neary = max(sy-l,1)
        idxnow = bisect_left(dcol[sx], sy)
        idxnear = bisect_left(dcol[sx], neary)
        #print(sy, neary, idxnow,idxnear,drow[sx])
        
        if idxnow==idxnear:
            sy = neary
        else:
            sy = dcol[sx][idxnow-1]+1
    elif d=="D":
        neary = min(sy+l, H)
        idxnow = bisect(dcol[sx], sy)
        idxnear = bisect(dcol[sx], neary)
        #print(sy, neary, idxnow,idxnear,drow[sx])
        
        if idxnow==idxnear:
            sy = neary
        else:
            sy = dcol[sx][idxnow]-1
            
    elif d=="R":
        neary = min(sx+l, W)
        idxnow = bisect(drow[sy], sx)
        idxnear = bisect(drow[sy], neary)
        #print(sx, neary, idxnow,idxnear)
        
        if idxnow==idxnear:
            sx = neary
        else:
            sx = drow[sy][idxnow]-1
            
    else:
        neary = max(sx-l, 1)
        idxnow = bisect_left(drow[sy], sx)
        idxnear = bisect_left(drow[sy], neary)
        #print(sx, neary, idxnow,idxnear)
        
        if idxnow==idxnear:
            sx = neary
        else:
            sx = drow[sy][idxnow-1]+1
    print(sy,sx)