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
A=LIST()

def prime_fac(A):
    d = defaultdict(int)
    cnt_zero=0
    for i in range(len(A)):
        a = A[i]
        if a==0:
            cnt_zero+=1
            continue
        
        x = 1
        for j in range(2, int(sqrt(a)+1)):
            cnt_j=0
            while a % j ==0:
                cnt_j+=1
                a //= j
            temp = cnt_j%2*j
            if temp != 0:
                x *=temp

            if a == 1:
                break
            
        if a !=1:
            x *= a
        d[x]+=1
    return d, cnt_zero


d, cnt_zero = prime_fac(A)
not_zero = N-cnt_zero
ans = cnt_zero*(cnt_zero-1)//2
ans += cnt_zero * not_zero
#print(ans)
for i in d:
    if d[i] <= 1:
        continue
    else:
        ans += d[i]*(d[i]-1)//2
print(ans)

