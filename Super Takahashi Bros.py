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
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N=INT()
A,B,X=ZIP(N-1)

queue = [(0,0)]
cost_list = [INF for _ in range(N)]
cost_list[0]=0
while queue:
    cost, stage = heappop(queue)
    #print(cost_list)
    if cost_list[stage] < cost:
        continue
    if stage ==  N-1:
        break

    if cost_list[stage+1]>cost_list[stage]+A[stage]:
        cost_list[stage+1]=cost_list[stage]+A[stage]
        heappush(queue, (cost_list[stage+1],stage+1))
    if cost_list[X[stage]-1]> cost_list[stage]+B[stage]:
        cost_list[X[stage]-1]=cost_list[stage]+B[stage]
        heappush(queue, (cost_list[X[stage]-1],X[stage]-1))
print(cost_list[-1])

