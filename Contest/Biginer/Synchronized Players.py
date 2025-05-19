# D
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd, prod
from cmath import phase
from itertools import accumulate, chain, combinations, combinations_with_replacement, permutations, compress, dropwhile, takewhile, groupby, product, starmap
from functools import cmp_to_key,lru_cache
from operator import itemgetter, mul, xor
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush , heappop
from functools import reduce, lru_cache
from sortedcontainers import SortedSet, SortedList, SortedDict
from decimal import Decimal, ROUND_HALF_UP
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
def ROUND_OFF(X,k): return  (X // (10 ** k) + 5) // 10 * 10 ** (k + 1)
def YES(): return print("Yes")
def NO(): return print("No")
alph = 'abcdefghijklmnopqrstuvwxyz'
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


N=INT()
S=[]
p1 = None; p2=None
for i in range(N):
    s=input().strip()
    for j in range(len(s)):
        if s[j]=="P":
            if p1 is None:
                p1 = (i,j)
            else:
                p2 = (i,j)
    S.append(s)
    
visited = [False for _ in range(N**4)]
def cal_idx(p1, p2):
    return (p1[0]*N+p1[1])*N**2 + (p2[0]*N+p2[1])
visited[cal_idx(p1, p2)] = True

def move(p1,dy, dx):
    p1y = p1[0]; p1x = p1[1]
    if 0<=p1y+dy<N and S[p1y+dy][p1x]!="#":
        p1y += dy
    if 0<=p1x+dx<N and S[p1y][p1x+dx]!="#":
        p1x += dx
    
    return (p1y, p1x)

ans = INF
q = deque([(p1,p2,0)])
while q:
    p1, p2, cost = q.popleft()
   # print(cost, p1,p2,q,ans)
    for dy, dx in Dxy:
        np1 = move(p1, dy, dx)        
        np2 = move(p2, dy, dx)
        idx = cal_idx(np1, np2)
        if np1==np2:
            print(cost+1)
            exit()
        if visited[idx]: continue
        visited[idx] = True
        q.append((np1, np2,cost+1))

print(-1)
