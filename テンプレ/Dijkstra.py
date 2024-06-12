"""
問題:
https://atcoder.jp/contests/arc177/tasks/arc177_c
BとRどちらかのマスで構成されたグリッドがある。(左上から右下へ行くのにBを通る回数)+(右上から左下へ行くのにRを通る回数)
のminを求めよ。

方針:ダイクストラ使用した(01BFSではない)
今回はコストが0or1なのでcost配列は用意していない。board[dy+y][x+dx]==colで判断している
確定済みかどうかを実装してないからもしかしたらTLEになる？？？？
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


N = INT()
board = BOARD(N)


def count_parpull(s,g,col):
    distance = [[INF]*N for _ in range(N)]
    distance[s[0]][s[1]] = 0
    queue = [(0,s[0],s[1])]
    while queue:
        cur_dis,y,x = heappop(queue)
        for dx,dy in dxy:
            if 0<=x+dx<N and 0<=y+dy<N:
                near_dis = cur_dis+ (board[dy+y][x+dx]==col) #colだったら+1
                #print(near_dis)
                if near_dis < distance[dy+y][dx+x]:
                    distance[dy+y][dx+x] = near_dis
                    heappush(queue, (near_dis,dy+y,dx+x))
        #print(queue)
    return distance[g[0]][g[1]]

#print(count_parpull((0,0), (N-1,N-1), "B"))
#print(count_parpull((0,N-1), (N-1,0), "R"))
print(count_parpull((0,0), (N-1,N-1), "B") + count_parpull((0,N-1), (N-1,0), "R"))
        



