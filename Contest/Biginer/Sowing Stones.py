# A
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
def LIST(): return list(map(int, input().split()))
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

N,M=MAP()
X=LIST()
A=LIST()

B=[]
for i in range(M):
    B.append((X[i], A[i]))
B.sort(key=lambda x: x[0])
A = [B[i][1] for i in range(M)]
X = [B[i][0] for i in range(M)]


d = 0
ans =0
if X[0]!=1:
    print(-1)
    exit()
if sum(X)!=N:
    print(-1)
    exit()

for i in range(M):
    if i==M-1:
        Xi, Xi1 = X[i], N+1
    else:
        Xi, Xi1 = X[i], X[i+1]
    a = A[i]-1
    
    diff = Xi1 - Xi -1

    ans+=diff*(diff+1)//2
    a-=diff
    if a>0:
        d += a
    else:
        ans = 
        while a<0:
            B, j = d.pop()
            if B>=-a:
                ans+=-a*(i-j)
                if B>-a:
                    d.append((B+a, j))
                break
            else:
                ans+=B*(i-j)
                a+=B
            
            if not d:
                print(-1)
                exit()

print(ans)