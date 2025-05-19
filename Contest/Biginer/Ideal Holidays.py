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

N,A,B=MAP()
D=LIST()
#Dのminとmaxのrange1が休日A以下ならOK

kagen=INF
jyougen=-INF
s=set()
for i in D:
    i=i%(A+B)
    s.add(i)
sorted_s = sorted(s)

for i in range(len(sorted_s)-1):
    if sorted_s[i+1]-sorted_s[i]>B:
         print("Yes")   
    kagen=min(kagen,sorted_s[i])
    jyougen=max(jyougen,sorted_s[i])
if jyougen-kagen+1 <= A:
    print("Yes")

else:
    print("No")