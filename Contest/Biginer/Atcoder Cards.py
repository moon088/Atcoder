# C
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
def LIST_3D(n): return [[LIST() for _ in range(n)] for _ in range(n)] #Axyz is (y*z)*x
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return map(list, zip(*(map(int, input().split()) for _ in range(n))))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def BOARD_INT(H): return [list(map(int, input().split())) for _ in range(H)]
def isInBoard(H,W,y,x): return 0<=y<=H and 0<=x<W
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


S=input()
T=input()
s = defaultdict(int)
t = defaultdict(int)
cnts=0
cntt=0
for i in S:
    if i=="@":
        cnts+=1
    else:
        s[i]+=1

for i in T:
    if i=="@":
        cntt+=1
    else:
        t[i]+=1

#print(cntt,cnts)
for i in s:
    #print(i,cntt)
    if s[i]<=t[i]:
        continue
    elif i in ["a", "t", "c", "o", "d", "e", "r"]:
        cntt-=abs(s[i]-t[i])
    else:
        exit(NO())
        
    if cntt<0:
        exit(NO())
        #print(i,cntt)
    

for i in t:
    if s[i]>=t[i]:
        continue
    elif i in ["a", "t", "c", "o", "d", "e", "r"]:
        cnts-=abs(s[i]-t[i])
    else:
        exit(NO())
    if cnts<0:
        exit(NO())
YES()
