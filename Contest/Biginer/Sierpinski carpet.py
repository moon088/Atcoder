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

N=INT()
board=[[None]*(3**N) for _ in range(3**N)]

def make_black(K,y,x):
    for i in range(3**K):
        for j in range(3**K):
            board[y+i][x+j]="."

def make_lebelK(K,y,x):#右上
    if K == 0:
        board[y][x]="#"
    else:
        for i in range(9):
            down_lebel=3**(K-1)
            #print(down_lebel*(i//3), down_lebel*(i%3))
            if i ==4:
                make_black(K-1,y+down_lebel*(i//3),x+down_lebel*(i%3))
            else:
                make_lebelK(K-1, y+down_lebel*(i//3), x+down_lebel*(i%3))

make_lebelK(N,0,0)
for i in range(3**N):
    for j in range(3**N):
        print(board[i][j],end="")
    print()
