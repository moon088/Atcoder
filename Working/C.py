# C
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
from more_itertools import run_length
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


N=INT()
A=LIST()
B = []
for i in range(N-1):
    if A[i]<A[i+1]:
        B.append("<")
    elif A[i]==A[i+1]:
        B.append("=")
    else:
        B.append(">")

ans = 0
left = 0
right=1
up = False; down = False
for left in range(N-3):
   # print(left, right, up, down, ans)
    if left>=right: right = left
    if B[left-1]=="<" and B[left]==">": up = False
    if B[left-1]==">"and B[left]=="<": down = False
    if B[left]!="<": continue
    if (right-left+1)>=4 and B[left]=="<" and down and up:
            ans += 1

    while right <N-1:
       # print(left, right, up, down, ans)
        kigou = B[right]
        if (right-left+1)>=2: 
            if B[right-1]=="<" and B[right]==">":
                if up: break
                up = True
            if B[right-1]==">"and B[right]=="<":
                if down: break
                down = True
        right+=1 
        
        if (right-left+1)>=4 and B[left]=="<" and down and up:
            ans += 1
print(ans)