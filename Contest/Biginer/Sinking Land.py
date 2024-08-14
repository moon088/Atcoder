# E
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
from cmath import phase
from itertools import accumulate, chain, combinations, combinations_with_replacement, permutations, compress, dropwhile, takewhile, groupby, product, starmap
from functools import cmp_to_key
from operator import itemgetter, mul, xor
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
def BOARD_INT(H): return [list(map(int, input().split())) for _ in range(H)]
def BOARD_INT(H): return [list(map(int, input().split())) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

"""_summary_
方針:Y個のキューを用意し、最終的にそのキューQkに入っているサイズがk年目で沈む面積となる。
    行う処理:キューQkから取り出した要素が初めて海に面したとき、
    A<=kならばQkに格納。A>kならばA年目で沈むのでQ_Aに格納を繰り返す
"""
MAX_Y = 10**5
H,W,Y=MAP()
#board = BOARD_INT(H)
board = [[0]*W for _ in range(H)]
Q = [deque() for _ in range(MAX_Y)]
visit = [[True]*W for _ in range(H)] #陸がTrue
for i in range(H):
    board[i] = list(map(int, input().split()))  # 標高データの入力
    for j in range(W):
        if i == 0 or i == H - 1 or j == 0 or j == W - 1:  # 端の処理
            Q[board[i][j]-1].append((i,j))
            visit[i][j] = False
        

"""for i in range(H):
    for j in [0,W-1]:
        Q[board[i][j]-1].append((i,j))
        visit[i][j] = False
        
for i in [0, H-1]:
    for j in range(1,W-1):
        Q[board[i][j]-1].append((i,j))
        visit[i][j] = False"""
         
         
         
#print(Q)
ans = H*W
for i in range(Y):
    q = Q[i]
    while q:
        ans -= 1
        y,x = q.popleft()
        
        for dy,dx in Dxy:
            near_x = x+dx
            near_y = y+dy
            if 0<=near_y<H and 0<=near_x<W and visit[near_y][near_x]:
                Q[max(board[near_y][near_x]-1,i)].append((near_y, near_x))
                visit[near_y][near_x] = False
    print(ans)

#print(visit)


