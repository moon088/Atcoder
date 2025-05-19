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

class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)  # 1-indexedで管理

    # idx(0-indexed) の位置に x を加算
    def add(self, idx, x):
        i = idx + 1  # 1-indexedに変換
        while i <= self.n:
            self.data[i] += x
            i += i & -i  # iの最下位ビットを加算

    # [0, idx] の累積和を求める (idxは0-indexed)
    def sum(self, idx):
        s = 0
        i = idx + 1  # 1-indexedに変換
        while i > 0:
            s += self.data[i]
            i -= i & -i  # iの最下位ビットを減算
        return s

    # [l, r) の区間和を求める (l, rは0-indexed)
    def range_sum(self, l, r):
        return self.sum(r - 1) - (self.sum(l - 1) if l > 0 else 0)


N,M=MAP()
A,B=ZIP(M)
Q=INT()
C,D=ZIP(Q)
mapping_b = [[] for _ in range(2*N)]
query = [[] for _ in range(2*N)]
bit = BIT(2*N)
ans = [None]*(Q)

for i in range(M):
    a,b=A[i]-1,B[i]-1
    bit.add(a, 1)
    bit.add(b, 1)
    mapping_b[b].append(i)
for i in range(Q):
    c,d=C[i]-1,D[i]-1
    query[d].append(i)

for d in range(1,2*N):#d決め打ってBIT更新しながらクエリ処理をする
    for idx in mapping_b[d-1]: #d超えたものの区間[Aj, Bj]のBIT更新をする
        a,b = A[idx]-1,B[idx]-1
        bit.add(a, -2)
 
    for q in query[d]:
        c,d=C[q]-1,D[q]-1
        ans[q] = bit.range_sum(c, d+1)

for i in range(Q):
    print(ans[i])
        