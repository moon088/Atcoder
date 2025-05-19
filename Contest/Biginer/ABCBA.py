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


"""
# Zargorism
def z_algorithm(s):
    n = len(s)
    Z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > r:
            l, r = i, i + Z[i] - 1
    return Z

S=input()
n = len(S)
T = S[::-1]+S
Z = z_algorithm(T)
ans = INF
for i in range(2*n-1,n-1,-1):
    if Z[i]==2*n-i:
        ans = 2*n-i    
rev = S[::-1]
print(S+rev[ans:])"""

# ローリングハッシュ
class RollingHash:
    def __init__(self, s, base=1007, mod=2**61 - 1):
        self.n = len(s)
        self.base = base
        self.mod = mod
        self.power = [1] * (self.n + 1)  # B^i の事前計算
        self.hash = [0] * (self.n + 1)   # prefix hash（0-indexed）

        for i in range(self.n):
            self.power[i+1] = self.power[i] * self.base % self.mod
            self.hash[i+1] = (self.hash[i] * self.base + ord(s[i])) % self.mod

    # [l, r) のハッシュを返す
    def get_hash(self, l, r):
        result = (self.hash[r] - self.hash[l] * self.power[r - l]) % self.mod
        # Pythonでは負になることもあるので補正
        if result < 0:
            result += self.mod
        return result
S=input()
rh_S = RollingHash(S)
rev_S = S[::-1]
rh_revS = RollingHash(rev_S)
ans = INF
for i in range(len(S)):
    if rh_S.get_hash(len(S)-i-1,len(S)) == rh_revS.get_hash(0, i+1):
        ans = i

print(S+rev_S[ans+1:])