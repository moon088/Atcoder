#D
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
from cmath import phase
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from functools import cmp_to_key
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush , heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

def inv(bunbo, bunshi, mod):
    return bunshi * pow(bunbo, mod - 2, mod) % mod

x = INT()
N = len(str(x))

mod = 998244353

print(inv(pow(10, N, mod) - 1, x * (pow(10, x * N, mod) - 1), mod))

"""
解説:
V_X = X + X*10^N + ... + X*10^{(N-1)K}
    = X{10^(NX)-1}/(10^N-1) (\bacause 等比数列の和)
    
(bunshi) = X * pow(10 , N*X, mod) - 1    <-easy
(bunbo) -> mod p上での逆元bunbo^(-1)を計算する

ここで逆元の計算はフェルマーの小定理
    aとpが互いに素=>a^(p-1)=1  (mod p)
                <=>a^(-1)=a^(p-2)  (mod p)

これよりbunboの逆元はbunbo^(p-2)を計算すればいい

よって
V_N = X * {pow(10, N*X, mod) -1} / {10^N-1}^(mod-2)
で計算できる
"""

