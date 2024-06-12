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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N,M,K=MAP()
C=[]
A=[]
R=[]
for i in range(M):
    temp=MIXED_LIST()
    C.append(temp.pop(0))
    R.append(temp.pop(C[i]))

    A.append(temp)
#print(A,C,R)

def judge(bits):
    for i in range(M):
        count=0
        for j in range(C[i]):
            if bits[A[i][j]-1]==1:
                count+=1
        if R[i]=="o":
            if count>=K:
                continue
            else:
                return 0
        else:
            if count>=K:
                return 0
            else:
                continue
    return 1
          
ans=0
for pro in product((0,1), repeat=N):
    #print(pro, judge(pro))
    ans+=judge(pro)
print(ans)