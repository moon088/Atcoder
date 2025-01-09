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

memo = {}
def sub_calc(n,R,c):
    """
    n桁で全部c未満かつR以下
    """
    if (n,R,c) in memo:
        return memo[n,R,c]
    if n == 0:
        return 1
    
    res = 0
    for d in range(c):
        if d <= R:
            res += sub_calc(n-1,(R-d)//10,c)
    memo[n,R,c] = res
    return res



def calc(R):
    if R < 10:
        return 0
    res = 0
    D = len(str(R))
    S = str(R)
    for d in range(2,D):
        for c in range(1,10):
            res += pow(c,d-1)
    
    for c in range(1,int(S[0])):
        res += pow(c,D-1)
    res += sub_calc(D-1,(R-int(S[0])*10**(D-1)),int(S[0]))
    return res

def solve(L,R):
    return calc(R) - calc(L-1)

L,R = MAP()
print(solve(L,R))