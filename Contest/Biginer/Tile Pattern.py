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

N,Q=MAP()
P = BOARD(N)

cum = [[0]*(N) for i in range(N)]
for i in range(N):
    for j in range(N):
        if P[i][j] == "B":
            cum[i][j] = 1
        if j!=0:
            cum[i][j] += cum[i][j-1]
for j in range(N):
    for i in range(1,N):
        cum[i][j] += cum[i-1][j]

def calc(h,w):
    h,w = h + 1, w + 1
    qh,qw = h//N,w//N
    rh,rw = h % N, w % N
    res = cum[-1][-1] * qh * qw
    if rh and rw:
        res += cum[rh-1][rw-1]
    if rw:
        res += cum[N-1][rw-1] * qh
    if rh:
        res += cum[rh-1][N-1] * qw
    return res


for _ in range(Q):
    a,b,c,d = MAP()

    res = calc(c,d) - calc(a-1,d) - calc(c,b-1) + calc(a-1,b-1)
    print(res)
    
