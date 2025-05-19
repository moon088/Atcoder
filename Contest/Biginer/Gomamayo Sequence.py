#D
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

"""
#方針 dp[i][j][k]:=i文字目まででi番目の文字がj,隣接回数がkであるminコスト
更新方法:i+1文字目を更新
#第2,3 idxの更新方法はS[i+1]==0->[0][0]はそのままS[i+1][0][0],[1][0]なら[i+1][1][0]+C
                                 [0][1]ならmin([i][0][0],[i][1][1])
                                 [1][0]なら[i][0][0]+C
                                 [1][1]なら[i][1][0]+C,[i][0][1]
"""                                 
N=INT()
S=input()
C=LIST()

dp = [[[INF]*2 for _ in range(2)] for _ in range(N)]
#print(dp)

if S[0]=="0":
    dp[0][0][0]=0
    dp[0][1][0]=C[0]
else:
    dp[0][0][0]=C[0]
    dp[0][1][0]=0
    

for i in range(1,N):
    if S[i] == '0':
        dp[i][0][0] = dp[i - 1][1][0]
        dp[i][0][1] = min(dp[i - 1][0][0], dp[i - 1][1][1])
        dp[i][1][0] = dp[i - 1][0][0] + C[i]
        dp[i][1][1] = min(dp[i - 1][0][1], dp[i - 1][1][0]) + C[i]
    else:
        dp[i][1][0] = dp[i - 1][0][0]
        dp[i][1][1] = min(dp[i - 1][1][0], dp[i - 1][0][1])
        dp[i][0][0] = dp[i - 1][1][0] + C[i]
        dp[i][0][1] = min(dp[i - 1][1][1], dp[i - 1][0][0]) + C[i]
ans = min(dp[N - 1][0][1], dp[N - 1][1][1])
print(ans)