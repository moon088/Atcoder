# B
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


H,W,D=MAP()
board=BOARD(H)
yuka = []
for i in range(H):
    for j in range(W):
        if board[i][j]==".":
            yuka.append((i,j))

combs = list(combinations(yuka,2))

def search(x,y,s):
    for dy in range(-D, D + 1):  
        for dx in range(-D + abs(dy), D - abs(dy) + 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and board[ny][nx]==".":
                s.add((ny,nx))
    return s  
f = 0
for comb in combs:
    one = comb[0]
    two = comb[1]
    
    ans = search(one[1], one[0], set())
    #print(one,ans)
    ans = search(two[1], two[0], ans)
   # print(two,ans)
    f = max(f, len(ans))
print(f)
    