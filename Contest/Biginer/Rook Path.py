# E
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
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

MOD = 998244353
W,H,K=MAP()
x1,y1,x2,y2 = MAP()
dp = [0,0,0,0] #samey,samex,notsamexy, samexy

if x1==x2 and y1==y2:
    dp[3] = 1
elif x1==x2:
    dp[1]=1
elif y1==y2:
    dp[0]=1
else:
    dp[2]=1
for i in range(K):
    ndp = [0,0,0,0]
    #print(dp)
    for j in range(4):
        if j==0:
            ndp[0] += (W-2)*dp[0]
            ndp[1] += 0
            ndp[2] += (H-1)*dp[0]
            ndp[3] += 1*dp[0]
        elif j==1:
            ndp[0] += 0
            ndp[1] += (H-2)*dp[1]
            ndp[2] += (W-1)*dp[1]
            ndp[3] += 1*dp[1]
        elif j==2:
            ndp[0] += 1*dp[2]
            ndp[1] += 1*dp[2]
            ndp[2] += (H+W-4)*dp[2]
            ndp[3] += 0
        else:
            ndp[0] += (W-1)*dp[3]
            ndp[1] += (H-1)*dp[3]
            ndp[2] += 0
            ndp[3] += 0
        ndp[0]%=MOD; ndp[1]%=MOD; ndp[2]%=MOD; ndp[3]%=MOD
    dp = ndp
#print(dp)
print(dp[3]%MOD)