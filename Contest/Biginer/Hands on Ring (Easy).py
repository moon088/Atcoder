# B
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

N,Q=MAP()
H,T=[], []
for i in range(Q):
    h,t=input().split()
    H.append(h)
    T.append(int(t))

def move_right(r, l, new):
    if r>l:
        if l<new and new<=r:
            return r-new
        else:
            return new-r if new>=r else N-(r-new)
    else:
        if r<=new and new<l:
            return new-r
        else:
            return r-new if r>=new else N-(new-r)

def move_left(r, l, new):
    if r>l:
        if l<=new and new<r:
            return new-l
        else:
            return l-new if new<=l else N-(new-l)
    else:
        if r<new and new<=l:
            return l-new
        else:
            return new-l if new>=l else N-(l-new)

ans =0
r=2
l=1
for i in range(Q):
    if H[i]=="R":
        ans += move_right(r, l, T[i])
        r=T[i]
    else:
        ans += move_left(r, l, T[i])
        l=T[i]
print(ans)