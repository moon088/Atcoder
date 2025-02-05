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

N=INT()
T=0
T,X,A=ZIP(N)
T1=max(T)
sunuke = [defaultdict(lambda: [0]) for _ in range(T1+1)]
for i in range(N):
    t,x,a=T[i],X[i],A[i]
    sunuke[t][x] += [a]

    
dp = [[-INF]*5 for _ in range(T1+1)]
dp[0][0]=0

for i in range(1,T1+1):
    l = sunuke[i]
    for j in range(5):
        dp[i][j] = max(dp[i-1][j], dp[i][j])
        
        get = max(l[j])
        if j>0 and dp[i-1][j-1]>-INF:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+get)
        if j<4 and dp[i-1][j+1]>-INF:
            dp[i][j] = max(dp[i][j], dp[i-1][j+1]+get)
        
        if dp[i-1][j]>-INF:
            dp[i][j] = max(dp[i][j], dp[i-1][j]+get)

#print(dp)
print(max(dp[-1]) if max(dp[-1])>0 else 0)     
