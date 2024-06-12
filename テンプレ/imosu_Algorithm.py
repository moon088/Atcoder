"""
問題:
https://atcoder.jp/contests/abc188/tasks/abc188_d
すぬけプライムへの加入中は1日あたりC円を支払うことで、提供される全てのサービスを追加料金の支払いなしに利用できる。
すぬけプライムへの加入および脱退は1日ごとに自由にでき、サービスをN個を利用する。
i個目のサービスはa_i日目からb_i日目まで利用する。すぬけプライムに加入していない期間中は1日あたりc_i円を支払う必要があります。
サービスを利用するために高橋くんが支払う必要のある最小の合計金額を求めてください。
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

N,C=MAP()
event=defaultdict(int)
for i in range(N):
    a,b,c=MAP()
    b+=1
    event[a]+=c
    event[b]-=c

m=sorted(event.keys())
ans=0
r=0
p=0
for i in m:
    ans+=min(r,C)*(i-p)
    p=i
    r+=event[i]
print(ans)



