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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

shiro1 = [(0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0)]
shiro2 = [(5,5),(5,6),(5,7),(5,8),(6,5),(7,5),(8,5)]
N,M=MAP()
S=[]
for i in range(N):
    s=input()
    S.append(s)

def check(y,x):
   # print(x,y)
    for i in range(3):
        for j in range(3):
            if S[y+i][x+j]!="#":
                return False
    for i in range(y+6,y+9):
        for j in range(x+6, x+9):
            if S[i][j]!="#":
                return False
    for ni, nj in shiro1:
        if 0<=y+ni<N and 0<=x+nj<M:
            if S[y+ni][x+nj]!=".":
                return False
    for ni, nj in shiro2:
        if 0<=y+ni<N and 0<=x+nj<M:
            if S[y+ni][x+nj]!=".":
                return False
    return True


for i in range(N-8):
    for j in range(M-8):
        if check(i,j):
            print(i+1, j+1)
