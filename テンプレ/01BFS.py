"""
問題
https://atcoder.jp/contests/arc005/tasks/arc005_3
s->gまで行くとき#を2回まで超えることができる。このときgまでたどり着けるかどうか    
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


H,W = MAP()
board = BOARD(H)

for i in range(H):
    for j in range(W):
        if board[i][j] == "s":
            sx = j
            sy = i
        elif board[i][j] == "g":
            gx = j
            gy = i

#距離は#なら1、ほか0の重みとしてとらえる
queue = deque([(sx,sy)])
inf = 10**9
dis = [[inf]*W for _ in range(H)]
dis[sy][sx]=0

while queue:
    x,y = queue.popleft()
    for dx, dy in dxy:
        if 0<=x+dx<W and 0<=y+dy<H :
            #print(y+dy,x+dx)
            if dis[y+dy][x+dx] == inf:#未探索
                if board[y+dy][x+dx]=="#":
                    dis[y+dy][x+dx] = dis[y][x]+1
                    queue.append((x+dx,y+dy)) #右端にいれる
                else:
                    dis[y+dy][x+dx]=dis[y][x]
                    queue.appendleft((x+dx,y+dy)) #左端に入れる

if dis[gy][gx]<=2:
    print("YES")
else:
    print("NO")