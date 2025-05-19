# D
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

class LazySegTree:
    DEFAULT = {
        'min': 1 << 60,
        'max': -(1 << 60),
        'sum': 0,
        'prd': 1,
        'gcd': 0,
        'lcm': 1,
        '^': 0,
        '&': (1 << 60) - 1,
        '|': 0,
    }

    FUNC = {
        'min': min,
        'max': max,
        'sum': (lambda x, y: x + y),
        'prd': (lambda x, y: x * y),
        'gcd': gcd,
        'lcm': (lambda x, y: (x * y) // gcd(x, y)),
        '^': (lambda x, y: x ^ y),
        '&': (lambda x, y: x & y),
        '|': (lambda x, y: x | y),
    }

    def __init__(self, ls, mode='min', func=None, default=None):
        N = len(ls)
        if default is None:
            self.default = self.DEFAULT[mode]
        else:
            self.default = default
        if func is None:
            self.func = self.FUNC[mode]
        else:
            self.func = func

        self.N = N
        self.K = (N - 1).bit_length() #N-1bit長、セグ木の高さ
        self.N2 = 1 << self.K #葉の数
        self.data = [self.default] * (2 * self.N2) #セグ木のリスト、初期値はdefault
        self.lazy = [None] * (2 * self.N2) #lazy遅延配列

        for i in range(self.N):# 葉の構築
            self.data[self.N2 + i] = ls[i]
        self.build()

    def build(self):
        for i in range(self.N2 - 1, 0, -1): #親と子の演算
            self.data[i] = self.func(self.data[i << 1], self.data[i << 1 | 1])

    def _apply(self, idx, value):#遅延適用
        if value is None:
            return
        self.data[idx] = self.func(self.data[idx], value)
        if idx < self.N2:
            self.lazy[idx] = self.func(self.lazy[idx], value) if self.lazy[idx] is not None else value

    def _push(self, idx): #遅延伝播
        self._apply(idx << 1, self.lazy[idx])
        self._apply(idx << 1 | 1, self.lazy[idx])
        self.lazy[idx] = None

    def update_range(self, L, R, value): #区間更新
        L += self.N2
        R += self.N2
        l0, r0 = L, R

        while L < R:
            if L & 1:
                self._apply(L, value)
                L += 1
            if R & 1:
                R -= 1
                self._apply(R, value)
            L >>= 1
            R >>= 1
        L, R = l0, r0
        while L > 1:
            L >>= 1
            if self.lazy[L] is None:
                self.data[L] = self.func(self.data[L << 1], self.data[L << 1 | 1])
            else:
                self._push(L)
        while R > 1:
            R >>= 1
            if self.lazy[R] is None:
                self.data[R] = self.func(self.data[R << 1], self.data[R << 1 | 1])
            else:
                self._push(R)

    def query_range(self, L, R):#区間クエリ
        L += self.N2
        R += self.N2
        for i in range(self.K, 0, -1):
            if (L >> i) << i != L:
                self._push(L >> i)
            if (R >> i) << i != R:
                self._push(R >> i)
        vL = self.default
        vR = self.default
        while L < R:
            if L & 1:
                vL = self.func(vL, self.data[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.func(self.data[R], vR)
            L >>= 1
            R >>= 1
        return self.func(vL, vR)



N, M=MAP()
X=LIST()
lazy = LazySegTree([0 for i in range(N+1)], mode = "sum")

for i in range(M-1):
    f, t = X[i], X[i+1]; f-=1; t-=1
    if f<t:
        lazy.update_range(f, t, N-(t-f))
        lazy.update_range(0,f, (t-f))
        lazy.update_range(t, N, (t-f))
    else:
        lazy.update_range(t, f, N-(f-t))
        lazy.update_range(0,t, (f-t))
        lazy.update_range(f, N, (f-t))
    
    
ans = INF    
for i in range(N):
    ans = min(ans, lazy.query_range(i,i+1))
print(ans)