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



#セグメント木のクラス
class SegTree:
    DEFAULT = {
        'min': 1 << 60,
        'max': -(1 << 60),
        'sum': 0,
        'prd': 1,
        'gcd': 0,
        'lmc': 1,
        '^': 0,
        '&': (1 << 60) - 1,
        '|': 0,
        "bool": False 
    }

    FUNC = {
        'min': min,
        'max': max,
        'sum': (lambda x, y: x + y),
        'prd': (lambda x, y: x * y),
        'gcd': gcd,
        'lmc': (lambda x, y: (x * y) // gcd(x, y)),
        '^': (lambda x, y: x ^ y),
        '&': (lambda x, y: x & y),
        '|': (lambda x, y: x | y),
        "bool": (lambda x, y: x or y) 
    }

    def __init__(self, ls, mode='min', func=None, default=None):
        """
        要素ls, 関数mode (min,max,sum,prd(product),gcd,lmc,^,&,|)
        func,defaultを指定すれば任意の関数、単位元での計算が可能
        """
        N = len(ls)
        if default == None:
            self.default = self.DEFAULT[mode]
        else:
            self.default = default
        if func == None:
            self.func = self.FUNC[mode]
        else:
            self.func = func
        self.N = N
        self.K = (N - 1).bit_length()  #N-1ビット長、セグ木の高さ
        self.N2 = 1 << self.K #葉の数
        self.size = self.N2 
        self.dat = [self.default] * (2**(self.K + 1)) #セグ木のリスト、初期値はdefault(単位元など)
        
        for i in range(self.N):  # 葉の構築
            self.dat[self.N2 + i] = (ls[i], -INF, 1, 0)
        self.build()

    def build(self):
        for j in range(self.N2 - 1, -1, -1):
            self.dat[j] = self.func(self.dat[j << 1], self.dat[j << 1 | 1])  # 親が持つ条件,左右の子の演算

    def leafvalue(self, x):  # リストのx番目の値
        return self.dat[x + self.N2]

    def update(self, x, y):  # index(x)をyに変更
        i = x + self.N2
        self.dat[i] = (y,-INF,1,0)
        while i > 0:  # 親の値を変更
            i >>= 1
            self.dat[i] = self.func(self.dat[i << 1], self.dat[i << 1 | 1])
        return

    def update_range(self, L, R, val):  # 区間[L, R)をvalに更新
        def _update_range(i, il, ir):
            if R <= il or ir <= L:
                return
            if L <= il and ir <= R:
                self.dat[i] = val  # 区間全体をvalに更新
                return
            mid = (il + ir) // 2
            _update_range(2 * i, il, mid)
            _update_range(2 * i + 1, mid, ir)
            self.dat[i] = self.func(self.dat[2 * i], self.dat[2 * i + 1])  # 親ノードを更新

        _update_range(1, 0, self.size)

    def query(self, L, R):  # [L,R)の区間取得
        L += self.N2
        R += self.N2
        vL = self.default
        vR = self.default
        while L < R:
            if L & 1:
                vL = self.func(vL, self.dat[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.func(self.dat[R], vR)
            L >>= 1
            R >>= 1
        return self.func(vL, vR)

    def __iter__(self):#リストなどの反復処理可能にするためイテラブルにしてる
        for i in range(self.N):
            yield self[i]

    def __getitem__(self, x): return self.leafvalue(x)
    def __setitem__(self, x, val): return self.update(x, val)
def mearge(x, y):
    vals = [
        (x[0], x[2]), (x[1], x[3]),
        (y[0], y[2]), (y[1], y[3])
    ]
    # 最大2個まで
    v1 = (-1, -1)  # (value, count)
    v2 = (-1, -1)
    for v, c in vals:
        if v == v1[0]:
            v1 = (v, v1[1] + c)
        elif v == v2[0]:
            v2 = (v, v2[1] + c)
        else:
            if v > v1[0]:
                v2 = v1
                v1 = (v, c)
            elif v > v2[0]:
                v2 = (v, c)
    return (v1[0], v2[0], v1[1], v2[1])

N,Q=MAP()
A=LIST()
seg_tree = SegTree(A, mode="max", func=mearge, default=(0,0,0,0))
for i in range(Q):
    a=LIST()
    #print(seg_tree.dat)
    if a[0]==1:
        p, x= a[1], a[2]
        seg_tree.update(p-1, x)
    else:
        l, r = a[1], a[2]
        a= seg_tree.query(l-1, r)
        print(a[3])
    