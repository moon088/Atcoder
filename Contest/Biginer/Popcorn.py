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


N,M=MAP()
S=[]
for _ in range(N):
    s=list(input().strip())
    S.append(s)

for i in range(N):
    for j in range(M):
        if S[i][j]=="o":
            S[i][j]=1
        else:
            S[i][j]=0

def make_all_cmb(N):
    all_cmb = []
    for i in range(1, N + 1):
        cmb = list(combinations(range(N), i))
        all_cmb.extend(cmb)
    return all_cmb

all_cmb = make_all_cmb(N)
#print(all_cmb)
for i in range(len(all_cmb)):
    temp=[0]*M
    
    for x in all_cmb[i]:        
        idx = x        
        for k in range(M):
            temp[k]=temp[k]|S[idx][k]
        
        if all(ele==1 for ele in temp):
            print(len(all_cmb[i]))
            exit()
