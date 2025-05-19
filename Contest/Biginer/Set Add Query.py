#E
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


N,Q=MAP()
x=LIST()
A=[0]*N
S=set()

log = defaultdict(list)
ruisekiwa = [0]
#|S|の累積和
for i in range(len(x)):
    if x[i] not in S:
        log[x[i]].append((i,Q,1))#1は後ろまで累積
        S.add(x[i])
    else:
        temp = log[x[i]].pop()
        log[x[i]].append((temp[0],i,-1))#-1は区間を計算済み
        S.remove(x[i])
    ruisekiwa.append(len(S)+ruisekiwa[-1])
    #print(log,S,ruisekiwa)
    
for i in range(1,N+1):
    for j in log[i]:
        if j: 
            #print(i,j)
            A[i-1] += ruisekiwa[j[1]] - ruisekiwa[j[0]]
            #print(A)
for i in A:
    print(i,end=" ")