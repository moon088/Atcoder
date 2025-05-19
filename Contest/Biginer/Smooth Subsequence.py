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

#dp[i]:=末尾iとなるものの長さ
#でもA[j]が末端となる更新時にv=A[j]-d~~A[j]+dまでの値を参照してd[v]を決定することになる->これはオーダーN^2となる
#そこでA[j]-d==A[j]+dを参照するときにlogNでいけるセグ木をそこで使う。
#つまりノードの値を部分列の長さとする

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
        self.dat = [self.default] * (2**(self.K + 1)) #セグ木のリスト、初期値はdefault(単位元など)
        
        for i in range(self.N):  # 葉の構築
            self.dat[self.N2 + i] = ls[i]
        self.build()

        """
        ls = [1, 3, 5, 7, 9, 11]のとき
        # self.dat = [default, default, default, default, default, default, default, default, 
        #           1, 3, 5, 7, 9, 11, default, default]
        """

    def build(self):
        for j in range(self.N2 - 1, -1, -1):
            self.dat[j] = self.func(self.dat[j << 1], self.dat[j << 1 | 1])  # 親が持つ条件,左右の子の演算

    def leafvalue(self, x):  # リストのx番目の値
        return self.dat[x + self.N2]

    def update(self, x, y):  # index(x)をyに変更
        i = x + self.N2
        self.dat[i] = y
        while i > 0:  # 親の値を変更
            i >>= 1
            self.dat[i] = self.func(self.dat[i << 1], self.dat[i << 1 | 1])
        return

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
    
    
    
N,D=MAP()
A=LIST()
MAX=max(A)
ls = [0]*(MAX+10)
seg = SegTree(ls, mode="max")

for i in A:
    l = max(i-D,0)
    r = min(i+D,MAX)
    tmp = seg.query(l,r+1)+1
    seg.update(i,tmp)
print(seg.query(0,MAX+1))

    


