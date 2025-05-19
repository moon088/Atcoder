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


N,M=MAP()
A=LIST()
if M==0:
    print(M)
    exit()
U,V=ZIP(M)
cost = [0]*N
g = [[] for _ in range(N)]
for i in range(M):
    u,v=U[i]-1,V[i]-1
    g[u].append(v); g[v].append(u)
    cost[u] += A[v]; cost[v] += A[u]    

def is_ok(val, cost):
    costs = cost.copy()
    ok = deque([])
    done = [False]*N
    for i in range(N):
        if costs[i]<=val:
            ok.append(i)
            done[i] = True
    while ok:
        now = ok.pop()
        for near in g[now]:
            if not done[near]:
                costs[near] -= A[now]
                if costs[near] <= val:
                    ok.append(near)
                    done[near] = True
    return all(done[i] for i in range(N))
        
    

l=0; r=INF
while (r-l)>1:
    mid = (r+l)//2
    if is_ok(mid, cost):
        r = mid
    else:
        l = mid
print(r)