<<<<<<< HEAD
# E
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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60



H,W,N=MAP()
R,C,L=ZIP(N)

class SegmentTree:
    def __init__(self, n, w):
        self.n = n
        self.w = w
        self.size = 1 << (n - 1).bit_length()
        self.data = [(True, INF, -INF)] * (2 * self.size)

    def _update(self, i):
        self.data[i] = (self.data[2 * i][0] and self.data[2 * i + 1][0] and
                        self.data[2 * i][2] <= self.data[2 * i + 1][1] - self.w,
                        min(self.data[2 * i][1], self.data[2 * i + 1][1]),
                        max(self.data[2 * i][2], self.data[2 * i + 1][2]))

    def place(self, l, r):  # [l, r) に配置
        def _place(i, il, ir):
            if r <= il or ir <= l:
                return
            if l <= il and ir <= r:
                self.data[i] = (False, il, ir + self.w - 1)
                return
            mid = (il + ir) // 2
            _place(2 * i, il, mid)
            _place(2 * i + 1, mid, ir)
            self._update(i)

        _place(1, 0, self.size)

    def can_place(self, l, r):  # [l, r) に配置できるか
        def _can_place(i, il, ir):
            if r <= il or ir <= l:
                return True
            if l <= il and ir <= r:
                return self.data[i][0] and self.data[i][1] >= r + self.w - 1 and self.data[i][2] <= l - self.w
            mid = (il + ir) // 2
            return _can_place(2 * i, il, mid) and _can_place(2 * i + 1, mid, ir)

        return _can_place(1, 0, self.size)

# 使用例
W = 5
seg_tree = SegmentTree(10, W)  # 幅10の範囲を管理

seg_tree.place(2, 5)  # [2, 5) に配置
print(seg_tree.can_place(0, 2))  # True
print(seg_tree.can_place(5, 7))  # False
print(seg_tree.can_place(7, 10))  # True

seg_tree.place(7, 9)  # [7, 9) に配置
print(seg_tree.can_place(5, 7))  # False
=======
# E
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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60



H,W,N=MAP()
R,C,L=ZIP(N)

class SegmentTree:
    def __init__(self, n, w):
        self.n = n
        self.w = w
        self.size = 1 << (n - 1).bit_length()
        self.data = [(True, INF, -INF)] * (2 * self.size)

    def _update(self, i):
        self.data[i] = (self.data[2 * i][0] and self.data[2 * i + 1][0] and
                        self.data[2 * i][2] <= self.data[2 * i + 1][1] - self.w,
                        min(self.data[2 * i][1], self.data[2 * i + 1][1]),
                        max(self.data[2 * i][2], self.data[2 * i + 1][2]))

    def place(self, l, r):  # [l, r) に配置
        def _place(i, il, ir):
            if r <= il or ir <= l:
                return
            if l <= il and ir <= r:
                self.data[i] = (False, il, ir + self.w - 1)
                return
            mid = (il + ir) // 2
            _place(2 * i, il, mid)
            _place(2 * i + 1, mid, ir)
            self._update(i)

        _place(1, 0, self.size)

    def can_place(self, l, r):  # [l, r) に配置できるか
        def _can_place(i, il, ir):
            if r <= il or ir <= l:
                return True
            if l <= il and ir <= r:
                return self.data[i][0] and self.data[i][1] >= r + self.w - 1 and self.data[i][2] <= l - self.w
            mid = (il + ir) // 2
            return _can_place(2 * i, il, mid) and _can_place(2 * i + 1, mid, ir)

        return _can_place(1, 0, self.size)

# 使用例
W = 5
seg_tree = SegmentTree(10, W)  # 幅10の範囲を管理

seg_tree.place(2, 5)  # [2, 5) に配置
print(seg_tree.can_place(0, 2))  # True
print(seg_tree.can_place(5, 7))  # False
print(seg_tree.can_place(7, 10))  # True

seg_tree.place(7, 9)  # [7, 9) に配置
print(seg_tree.can_place(5, 7))  # False
>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(seg_tree.can_place(0, 2))  # False