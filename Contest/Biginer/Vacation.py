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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N = INT()
cost = [[], [], []]
for i in range(N):
    a,b,c=MAP()
    cost[0].append(a)
    cost[1].append(b)
    cost[2].append(c)

dp = [[-INF]*3 for _ in range(N)]
#print(cost)
dp[0][0],dp[0][1],dp[0][2]=cost[0][0],cost[1][0],cost[2][0]

#i日目に遊びjをしたときの最大幸福度
for i in range(N-1):
    for j in range(3):
        if j == 0:
            dp[i+1][0] = max(dp[i+1][0], dp[i][1]+cost[0][i+1], dp[i][2]+cost[0][i+1])  
        elif j == 1:
            dp[i+1][1] = max(dp[i+1][1], dp[i][0]+cost[1][i+1], dp[i][2]+cost[1][i+1])  
        else:
            dp[i+1][2] = max(dp[i+1][2], dp[i][0]+cost[2][i+1], dp[i][1]+cost[2][i+1])  
ans = max(dp[-1])
#print(dp)
print(ans)