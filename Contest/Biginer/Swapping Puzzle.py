# D
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
#sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def list_input(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def BOARD_INT(H): return [list(map(int, input().split())) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

H,W=MAP()
A = BOARD_INT(H)
B = BOARD_INT(H)

def to_tuple(a):
    return tuple(tuple(r) for r in a)
d = {to_tuple(A): 0}
q = deque([A])
while len(q) > 0:
    a = q.popleft()
    for i in range(H - 1):
        b = deepcopy(a)
        b[i], b[i + 1] = b[i + 1], b[i]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            q.append(b)
    for j in range(W - 1):
        b = deepcopy(a)
        for i in range(H):
            b[i][j], b[i][j + 1] = b[i][j + 1], b[i][j]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            q.append(b)
print(d[to_tuple(B)] if to_tuple(B) in d else -1)