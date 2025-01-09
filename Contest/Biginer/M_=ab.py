# D
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
from sortedcontainers import SortedSet, SortedList, SortedDict
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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

"""def isOK(index):
   # print(index)
    a = index
    left = a
    right = N
    if a**2>=M:
        return True, (a,a)
    elif a*N<M:
        return False,[]
    
    while abs(right-left)>1:
       # print(right,left,132)
        b = (right+left)//2
        if a*b>=M:
            right = b
        else:
            left = b
            
    return  [True, (a,left)] if a*left>=M else [True, (a,right) ]   

def binary_search():
    ng = 0
    ok = N+1
    ans=N**2
    while abs(ok - ng) > 1:  
        mid = (ok + ng) // 2
        temp = isOK(mid)
       # print(temp)
        flag = temp[0]
        if flag:
            ok = mid
            ans = min(ans, temp[1][0]*temp[1][1])
        else:
            ng = mid
    return ans

N,M=MAP()

if N**2<M:
    print(-1)
    exit()
    
ans = binary_search()
print(ans)
"""

N,M=MAP()
a=1
ans=INF
for i in range(1, N + 1):
    x = (M+1)//i + 1 
    if x <= N:
        ans = min(ans, i * x)
    if i > x:
        break
print(-1 if ans == INF else ans)