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


N,K=MAP()
A=LIST()
if N//2>K:
    ans = 0
    now = -1
    for a in A:
        now = max(now, a.bit_length())

    S = list(combinations(range(N), K))
    while now>=0:
        ok = set()
        for eles in S:
            cnt =0
            for ele in eles:
                if A[ele]>>now &1:
                    cnt+=1
            if cnt&1:
                ok.add(eles)
        if len(ok)>0:
            S = ok
            ans += 1<<now
        
        now -= 1
    print(ans)
else:
    ans = 0
    now = -1
    all_xor = [0]*65
    for a in A:
        now = max(now, a.bit_length())
        for i in range(a.bit_length()):
            all_xor[i] ^= (a>>i)&1
    K = N-K
    S = list(combinations(range(N), K))
    while now >=0:
        ok = set()
        if all_xor[now]==1:
            f = 0
        else:
            f = 1
        for eles in S:
            cnt = 0 
            for ele in eles:
                if (A[ele]>>now)&1:
                    cnt+=1
            if cnt%2==f:
                ok.add(eles)
        if len(ok)>0:
            S = ok
            ans += 1<<now
        now -= 1
    print(ans)
