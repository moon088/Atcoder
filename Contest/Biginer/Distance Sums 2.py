# F
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
from more_itertools import run_length
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
g = [[] for _ in range(N)]
deg = [0]*N
for i in range(N-1):
    u, v = MAP(); u-=1; v-=1
    g[u].append(v); g[v].append(u)
    deg[u] += 1; deg[v] += 1
if N==2:
    print(1)
    print(1)
    exit()
    
num_child = [0]*N
visited = [False]*N
for i in range(N):
    if deg[i]!=1: 
        start = i
        break
def dfs(now):
    if deg[i]==1: 
        num_child[now] = 0
        return 0
    ans = 0
    for near in g[now]:
        if visited[near]: continue
        visited[near] = True
        ans += dfs(near) + 1
    num_child[now] = ans
    return ans
visited[start] = True
dfs(start)
visited = [False]*N; visited[start] = True
ans = [None]*N; temp = 0
q = deque([(start, 0)])
while q:
    now, depth = q.pop()
    temp += depth
    for near in g[now]:
        if visited[near]: continue
        q.append((near, depth+1))
        visited[near] = True
ans[start] = temp
#print(num_child, ans)


q = deque([(near, start) for near in g[start]])
while q:
    now, before = q.pop()
    ans[now] = ans[before] + (N-2-num_child[now]) - num_child[now]
    for near in g[now]:
        if ans[near] is not None: continue
        q.append((near, now))

for i in range(N):
    print(ans[i])
    