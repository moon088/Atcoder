"""
問題: 
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_s
n個の品物のi番目の重さと価値がそれぞれweight[i],value[i]のとき、
重さの総和がWを超えないように選びかつ、価値の総和maxを求めよ


方針:dp[i+1][w]:  dpサイズは(n+1)*(W+1)
初期条件はdp[0][w]=0
dp[i+1][w]= max(dp[i][w-weight[i]], dp[i+1][w])
"""

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

N,W=MAP()
weight,value=ZIP(N)
dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(W+1):
        if i==0:
            dp[i][j]=0
            continue
        
        w = weight[i-1]
        if w > j:
            dp[i][j]=dp[i-1][j]
            continue
        else:
            dp[i][j]= max(dp[i-1][j-w]+value[i-1], dp[i-1][j])
        #print(dp[i][j],(i,j))

#for i in range(N+1):
#    for j in range(W+1):
#        print(dp[i][j],end=" ")
#    print("")            
print(dp[N][W])            
            