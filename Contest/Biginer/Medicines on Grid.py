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
def BOARD_StoG(H):
    board, start, goal = [], None, None
    for i in range(H):
        row = list(input().strip()); board.append(row)
        if 'S' in row: start = (i, row.index('S'))
        if 'T' in row: goal = (i, row.index('T'))
    return board, start, goal
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

#heapqueueは最小要素を取り出し、再構成を行う。
# 今回はdistanceが残りhpのためhpが大きい順に取り出さないといけない。
# つまり-1倍してpushし、-1倍して取り出す必要がある

H,W=MAP()
A,s,g=BOARD_StoG(H)
N=INT()
hp=defaultdict(int)
for i in range(N):
    r,c,e=MAP()
    hp[(r,c)]=e

def count_parpull(s,g,map):
    distance = [[-1]*W for _ in range(H)]
    distance[s[0]][s[1]] = 0
    queue = [(0,s[0],s[1])]
    
    
    while queue:
        #print("pased",distance)
        cur_dis,y,x = heappop(queue)
        cur_dis = max(hp[(y+1,x+1)], -cur_dis)
        hp[(y+1,x+1)]=cur_dis
        if cur_dis<=0:
            continue
        #print(cur_dis)
        for dx,dy in dxy:
            if 0<=x+dx<W and 0<=y+dy<H and map[y+dy][x+dx]!="#":
                near_dis= cur_dis - 1
                #print(near_dis)
                if near_dis > distance[dy+y][dx+x]:
                    distance[dy+y][dx+x] = near_dis
                    heappush(queue, (-near_dis,dy+y,dx+x))
        #print(queue)
        #print(distance)
    return distance[g[0]][g[1]]


min_dis = count_parpull(s,g,A)
#print(min_dis)
if min_dis>=0:
    print("Yes")
else:
    print("No")
