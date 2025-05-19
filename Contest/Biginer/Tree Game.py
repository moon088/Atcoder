# E
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



N = INT()
gset = set()
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = MAP(); u-=1; v-=1
    graph[u].append(v)
    graph[v].append(u)
    gset.add((u,v))
    
colors = [-1] * N
q = deque([0]); colors[0] = 0
while q:
    u = q.popleft()
    for v in graph[u]:
        if colors[v] == -1:
            colors[v] = 1 - colors[u]
            q.append(v)
s=set()
for i in range(N):
    for j in range(i+1, N):
        if colors[i]!=colors[j] and (i, j) not in  gset and (j, i) not in gset:
            s.add((i+1,j+1))
if len(s)%2==1:
    print("First", flush=True)
    now = s.pop()
    print(now[0], now[1], flush=True)
else:
    print("Second", flush=True)

while True:
    x,y = MAP()
    if x==-1 and y==-1:
        exit()
    s.discard((x, y))
    s.discard((y, x))
    now = s.pop()
    print(now[0], now[1], flush=True)
