# C
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
def LIST_3D(n): return [[LIST() for _ in range(n)] for _ in range(n)] #Axyz is (y*z)*x
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return map(list, zip(*(map(int, input().split()) for _ in range(n))))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def BOARD_INT(H): return [list(map(int, input().split())) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1), (-1,-1),(-1,1),(1,-1),(1,1)]
INF = 1 << 60

H,W=MAP()
board = BOARD(H)
cnt=0
visited=[[False]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if board[i][j]=="." or visited[i][j]:
            continue
        elif board[i][j]=="#":
            cnt+=1
            visited[i][j]=True
            q = deque([(i,j)])
            while q:
                now = q.pop()
                board[now[0]][now[1]]=True
                for y,x in Dxy:
                    if 0<=now[0]+y<H and 0<=now[1]+x<W and not visited[now[0]+y][now[1]+x] and board[now[0]+y][now[1]+x]=="#":
                        q.append((now[0]+y, now[1]+x))
                        visited[now[0]+y][now[1]+x]=True
print(cnt)

import sys
from collections import deque

def input(): return sys.stdin.readline().strip()
def MAP(): return map(int, input().split())

Dxy = [(1,0),(-1,0),(0,1),(0,-1), (-1,-1),(-1,1),(1,-1),(1,1)]

H,W=MAP()
board = [list(input()) for _ in range(H)]
visited = [[False] * W for _ in range(H)]  # 訪問済みフラグ
cnt=0

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    while q:
        now = q.popleft()
        for y, x in Dxy:
            ny, nx = now[0] + y, now[1] + x
            if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == "#" and not visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = True

for i in range(H):
    for j in range(W):
        if board[i][j] == "#" and not visited[i][j]:
            cnt += 1
            bfs(i, j)

print(cnt)