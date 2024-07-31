# D
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
def list_input(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

#K桁の文字列1->10,2->10,3->10*10,4->100,5->1000,6->1000
N=INT()

if N == 1:
    print(0)
    exit(0)
N -= 1

i = 1
while True:
    p_nums = 9 * (10 ** ((i - 1) // 2))
    if N <= p_nums:
        break
    N -= p_nums
    i += 1

#print(i, N)

s = str(N + 10 ** ((i - 1) // 2) - 1)
#print(s)
if i % 2 == 0:
    print(s + s[::-1])
else:
    print(s[:-1] + s[::-1])
