<<<<<<< HEAD
# E
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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
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
            if L < self.N2 and self.lazy[L] is None:
                self.data[L] = self.func(self.data[L << 1], self.data[L << 1 | 1])
            else:
                self._push(L)
        while R > 1:
            R >>= 1
            if R < self.N2 and self.lazy[R] is None:
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
    
    
N,M=MAP()
A=LIST()
B=LIST()

lazy_segtree = LazySegTree(A, mode="sum")


for i in range(M):
    num_ball = lazy_segtree.query_range(B[i], B[i]+1)
    lazy_segtree.update_range(B[i], B[i]+1,-num_ball)
    quotient, remainder = divmod(num_ball, N)
    #print(num_ball, quotient, remainder)
    s=[]
    g=[]
    if remainder+B[i] <= N-1 and remainder!=0:
        s.append(B[i]+1)
        g.append(B[i]+remainder+1) 
    elif remainder+B[i]>= N and remainder!=0:
        s.append(B[i]+1)
        g.append(N)
        s.append(0)
        g.append(B[i]+remainder-N+1)
    #print(quotient, remainder,s,g)
    for si,gi in zip(s,g):
        lazy_segtree.update_range(si, gi, 1)
    if quotient:
        lazy_segtree.update_range(0,N,quotient)
    
for i in range(N):
    print(lazy_segtree.query_range(i,i+1), end=" ")
=======
# E
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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
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
            if L < self.N2 and self.lazy[L] is None:
                self.data[L] = self.func(self.data[L << 1], self.data[L << 1 | 1])
            else:
                self._push(L)
        while R > 1:
            R >>= 1
            if R < self.N2 and self.lazy[R] is None:
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
    
    
N,M=MAP()
A=LIST()
B=LIST()

lazy_segtree = LazySegTree(A, mode="sum")


for i in range(M):
    num_ball = lazy_segtree.query_range(B[i], B[i]+1)
    lazy_segtree.update_range(B[i], B[i]+1,-num_ball)
    quotient, remainder = divmod(num_ball, N)
    #print(num_ball, quotient, remainder)
    s=[]
    g=[]
    if remainder+B[i] <= N-1 and remainder!=0:
        s.append(B[i]+1)
        g.append(B[i]+remainder+1) 
    elif remainder+B[i]>= N and remainder!=0:
        s.append(B[i]+1)
        g.append(N)
        s.append(0)
        g.append(B[i]+remainder-N+1)
    #print(quotient, remainder,s,g)
    for si,gi in zip(s,g):
        lazy_segtree.update_range(si, gi, 1)
    if quotient:
        lazy_segtree.update_range(0,N,quotient)
    
for i in range(N):
    print(lazy_segtree.query_range(i,i+1), end=" ")
>>>>>>> 5a60e3f (Sync local Atcoder directory)
