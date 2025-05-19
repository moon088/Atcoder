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


N, P = MAP()
MOD = 998244353
two = (P*pow(100, -1, MOD))%MOD
one = (1-two)%MOD

if one ==0:
    print((N+1)//2)
    exit()
if two==0:
    print(N)
    exit()

def pre_comb(N):
    pre = [1] * (N+1)
    pre_inv = [1] * (N+1)

    for i in range(2, N+1):
        pre[i] = pre[i-1] * i % MOD

    pre_inv[N] = pow(pre[N], MOD-2, MOD)
    for i in range(N-1, 0, -1):
        pre_inv[i] = pre_inv[i+1] * (i+1) % MOD

    return pre, pre_inv


pre, pre_inv = pre_comb(N)
print(pre, pre_inv)
ans = 0
twocnt=0
while twocnt*2<=N:
    nowone = pow(one, N-2*twocnt, MOD)
    nowtwo = pow(two, twocnt, MOD)
    temp = (nowone*nowtwo * (N-twocnt))%MOD
    comb = (pre[N-twocnt]*pre_inv[twocnt]*pre_inv[N-2*twocnt])%MOD
    print(nowone, nowtwo,temp, comb)
    temp = (temp*comb)%MOD
    
    print(ans)
    ans =  (ans+temp)%MOD
    twocnt += 1


twocnt=0
while twocnt*2<=N-1:
    nowone = pow(one, N-1-2*twocnt, MOD)
    nowtwo = pow(two, twocnt+1, MOD)
    temp = (nowone*nowtwo*(N+1-twocnt))%MOD
    comb = (pre[N-1-twocnt]*pre_inv[twocnt]*pre_inv[N-1-2*twocnt])%MOD
    ans = (ans + temp*comb%MOD)%MOD
    twocnt += 1

print(ans%MOD)