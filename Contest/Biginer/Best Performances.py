# E
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd, prod
from cmath import phase
from itertools import accumulate, chain, combinations, combinations_with_replacement, permutations, compress, dropwhile, takewhile, groupby, product, starmap
from functools import cmp_to_key,lru_cache
from operator import itemgetter, mul, xor
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush , heappop
from functools import reduce, lru_cache
from sortedcontainers import SortedSet, SortedList, SortedDict
from decimal import Decimal, ROUND_HALF_UP
#it is code to make recursion a bit faster
#Pimport pypyjit
#pypyjit.set_param("max_unroll_recursion=-1")
#recursion limit
sys.setrecursionlimit(10**7)
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
def isInBoard(H,W,y,x): return 0<=y<H and 0<=x<W
def ROUND_OFF(X,k): return  (X // (10 ** k) + 5) // 10 * 10 ** (k + 1)
def YES(): return print("Yes")
def NO(): return print("No")
alph = 'abcdefghijklmnopqrstuvwxyz'
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


N, K, Q = MAP()
X, Y=ZIP(Q)
if N==1: 
    now=0
    for i in range(Q):
        now = Y[i]
        print(now)
    exit()
if N==K:
    ima = [0]*N
    s=0
    for i in range(Q):
        x,y=X[i], Y[i]
        temp = ima[x-1]
        s += y-temp
        ima[x-1]=y
        print(s)
    exit()

ueq = SortedList([0]*K)
sitaq = SortedList([0]*(N-K))
ima = [0]*N
s = 0
for i in range(Q):
    x,y=X[i], Y[i]
    de = ima[x-1]
    ima[x-1] = y

    if sitaq[-1]>=de:
        assert de in sitaq
        sitaq.discard(de)
    else:
        assert de in ueq
        ueq.discard(de)
        s -= de
    sitaq.add(y)
    while len(ueq)<K:
        temp = sitaq.pop(-1)
        ueq.add(temp)
        s += temp
    while sitaq[-1]>ueq[0]:
        temp1, temp2 = sitaq.pop(-1), ueq.pop(0)
        sitaq.add(temp2), ueq.add(temp1)
        s += temp1-temp2
    #print(ueq, sitaq, s, ima)
    print(s)
    