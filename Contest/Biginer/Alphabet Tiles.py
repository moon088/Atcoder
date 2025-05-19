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

class factorial():
    def __init__(self,n=0,mod=998244353):
        self.mod=mod
        self.fact_n=[1]
        self.fact_i=[1]
        self.fact_l=0
        self.create(n)
    
    def create(self,n):
        if self.fact_l<n:
            for i in range(self.fact_l+1,n+1):
                self.fact_n.append((self.fact_n[-1]*i)%self.mod)
                self.fact_i.append(0)
            self.fact_i[n]=pow(self.fact_n[n],-1,self.mod)
            for i in range(n,self.fact_l+1,-1):
                self.fact_i[i-1]=(self.fact_i[i]*i)%self.mod
            self.fact_l=n
        
    def fact(self,n):
        if n>self.fact_l:
            self.create(n)
        return self.fact_n[n]
    
    def fact_inv(self,n):
        if n>self.fact_l:
            self.create(n)
        return self.fact_i[n]

    def perm(self,n,r):
        if n<r:
            return 0
        if r<0:
            return 0
        return (self.fact(n)*self.fact_inv(n-r))%self.mod
    
    def comb(self,n,r):
        if n<r:
            return 0
        if r<0:
            return 0
        return (self.fact(n)*self.fact_inv(n-r)*self.fact_inv(r))%self.mod
    

MOD = 998244353
K=INT()
C=LIST()
dp = [0]*(K+1); dp[0]=1
f=factorial(K+10,MOD)
for i in range(26):
    kdp = [0]*(K+1)
    for j in range(K+1):
        for k in range(C[i]+1):
            if j+k>K: break
            kdp[j+k] += dp[j]*f.comb(K-i, j)
    for i in range(K+1):
        kdp[i]%=MOD
    dp = kdp

ans = 0
for i in range(1, K+1):
    ans += dp[i]*pow(f.comb(K, i), -1, MOD)
    ans %= MOD
print(ans)