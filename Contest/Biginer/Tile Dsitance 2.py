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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

"""A, B, C, D =map(int, input().split())
A+=10**9
B+=10**9
C+=10**9
D+=10**9

def make_sq(x, y):
    quo_x, remain_x =  divmod(x, 4)
    quo_y, remain_y =  divmod(y, 2)
    ans = 0
    ans += 8*quo_x*quo_y
    #print(ans)
    if remain_x>=1:
        ans+=quo_y *3
    if remain_x>=2:
        ans+=quo_y*3
    if remain_x>=3:
        ans+=quo_y
    if remain_y==1:
        ans+=quo_x*2
    if remain_y==1:
        if remain_x>=1:
            ans+=2
        if remain_x>=2:
            ans+=1
            
    print(ans)
    return ans


#make_sq(2000000000,2000000000)
#make_sq(3,3)
ans = make_sq(C, D) - make_sq(A, D) - make_sq(C, B) + make_sq(A, B)
print(ans)"""


