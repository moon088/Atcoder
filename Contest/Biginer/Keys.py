#C
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
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N,M,K=MAP()
C=[]
A=[]
R=[]
for i in range(M):
    c,*a,r=MIXED_LIST()
    C.append(c)
    A.append(a)
    R.append(r)
ans=0
for i in range(1<<N):
    flag=True
    for j in range(M):
        cnt=sum(1 for k in range(C[j]) if i&(1<<A[j][k]-1))
        if (cnt>=K and R[j]=="x") or (cnt<K and R[j]=="o"):
            flag=False
            break
    if flag:
        #print(i,j,cnt,bin(i))
        ans+=1
#print(i,j,cnt,bin(1<<N))
print(ans)
