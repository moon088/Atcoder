#C
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

N =INT()
box = []
for i in range(N):
    a,c=MAP()
    box.append((i+1,a,c))

box.sort(key=lambda x:x[1],reverse=True)
#print(box)
ans=[box[0][0]]
min=box[0][2]
for i in range(1,N):
    if  min >= box[i][2]:
        min = box[i][2]
        ans.append(box[i][0])
        #print(box[i][0])
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i],end=" ")
