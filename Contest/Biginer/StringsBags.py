<<<<<<< HEAD
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


#dp[i][j]:=i行目までを利用し、j番目までを作る文字列の最小コスト
T=input()
N=INT()
S=[]
for i in range(N):
    s=input().split()
    A=s.pop(0)
    S.append(s)
dp = [[INF for _ in range(len(T)+1)] for _ in range(N+1)]

dp[0][0]=0
for i in range(N):
    for j in range(len(T)+1):
        dp[i+1][j]=min(dp[i+1][j],dp[i][j])
        for k in S[i]:
            if T[j:j+len(k)]==k:
                dp[i+1][j+len(k)]=min(dp[i][j]+1, dp[i+1][j+len(k)])
            

if dp[N][len(T)]==INF:
    print(-1)
else:
    print(dp[N][len(T)])                   


=======
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


#dp[i][j]:=i行目までを利用し、j番目までを作る文字列の最小コスト
T=input()
N=INT()
S=[]
for i in range(N):
    s=input().split()
    A=s.pop(0)
    S.append(s)
dp = [[INF for _ in range(len(T)+1)] for _ in range(N+1)]

dp[0][0]=0
for i in range(N):
    for j in range(len(T)+1):
        dp[i+1][j]=min(dp[i+1][j],dp[i][j])
        for k in S[i]:
            if T[j:j+len(k)]==k:
                dp[i+1][j+len(k)]=min(dp[i][j]+1, dp[i+1][j+len(k)])
            

if dp[N][len(T)]==INF:
    print(-1)
else:
    print(dp[N][len(T)])                   


>>>>>>> 5a60e3f (Sync local Atcoder directory)
