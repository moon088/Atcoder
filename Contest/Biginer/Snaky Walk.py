# D
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
from sortedcontainers import SortedList
#it is code to make recursion a bit faster
#Pimport pypyjit
#pypyjit.set_param("max_unroll_recursion=-1")
#recursion limit
sys.setrecursionlimit(10**7)
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
def isInBoard(H,W,y,x): return 0<=y<H and 0<=x<W
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


H,W=MAP()
S=[]
for i in range(H):
    temp=input()
    S.append(temp)
    for j in range(len(temp)):
        if temp[j]=="S":
            s = (i,j)
        elif temp[j]=="G":
            g = (i,j)

visited = [[[INF, INF] for _ in range(W)] for _ in range(H)]

visited[s[0]][s[1]] = [0,0]

q = deque()
q.append((s[0], s[1], 0))
q.append((s[0], s[1], 1))
while q:
    i, j,dir = q.popleft() #dir0->縦,1->横
   # print(f"---{i,j,dir}")
    a = [Dxy[0],Dxy[1]] if dir==0 else [Dxy[2], Dxy[3]]
    for d in a:
        ni, nj = i+d[0], j+d[1]
        #print(ni,nj)
        if 0 <= ni < H and 0 <= nj < W:    
            if S[ni][nj] == "#": continue  
            #print(ni,nj)
            if visited[ni][nj][(dir+1)%2]  <= visited[i][j][dir]+1: continue 
            
            visited[ni][nj][(dir+1)%2] = visited[i][j][dir]+1
            q.append((ni, nj, (dir+1)%2))
ans = visited[g[0]][g[1]]

"""for i in range(H):
    print()
    for j in range(W):
        print(visited[i][j],end=" ")"""
print(min(visited[g[0]][g[1]]) if min(visited[g[0]][g[1]])<INF else -1)