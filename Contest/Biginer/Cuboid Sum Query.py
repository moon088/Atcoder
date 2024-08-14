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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def BOARD_INT(H): return [list(map(int, input().split())) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N=INT()

A = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
for z in range(1, N + 1):
    for x in range(1, N + 1):
        line = input().split()
        for y in range(1, N + 1):
            A[z][x][y] = int(line[y - 1]) 
#print(A)


cumsum = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for z in range(1, N + 1):
            cumsum[x][y][z] = A[x][y][z] + cumsum[x - 1][y][z] + cumsum[x][y - 1][z] + cumsum[x][y][z - 1] \
                              - cumsum[x - 1][y - 1][z] - cumsum[x - 1][y][z - 1] - cumsum[x][y - 1][z - 1] \
                              + cumsum[x - 1][y - 1][z - 1]

def query(lx, rx, ly, ry, lz, rz):
    #print(cumsum[rx][ry][rz] , cumsum[lx - 1][ry][rz] , cumsum[rx][ly - 1][rz] , cumsum[rx][ry][lz - 1] \
           #, cumsum[lx - 1][ly - 1][rz] , cumsum[lx - 1][ry][lz - 1] , cumsum[rx][ly - 1][lz - 1] \
           #, cumsum[lx - 1][ly - 1][lz - 1])
    return cumsum[rx][ry][rz] - cumsum[lx - 1][ry][rz] - cumsum[rx][ly - 1][rz] - cumsum[rx][ry][lz - 1] \
           + cumsum[lx - 1][ly - 1][rz] + cumsum[lx - 1][ry][lz - 1] + cumsum[rx][ly - 1][lz - 1] \
           - cumsum[lx - 1][ly - 1][lz - 1]
Q = INT()
queries = []
for _ in range(Q):
    Lx,Rx,Ly,Ry,Lz,Rz = MAP()
    print(query(Lx,Rx,Ly,Ry,Lz,Rz))