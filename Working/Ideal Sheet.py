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


Ha, Wa = MAP()
A = BOARD(Ha)
Hb, Wb = MAP()
B = BOARD(Hb)
Hx, Wx = MAP()
X = BOARD(Hx)

CNTA, CNTB=sum(A[i].count("#") for i in range(Ha)), sum(B[i].count("#") for i in range(Hb))

def check(X, board, cnta, cntb):
    for i in range(Hx):
        if X[i]!=board[i]: return False
    return cnta==CNTA and cntb==CNTB

for i in range(-11, 11):
    for j in range(-11, 11):
        for shify in range(-22, 22):
            for shifx in range(-22, 22):
                board = [[None]*Wx for _ in range(Hx)]
                cnta=0; cntb=0
                for h in range(Hx):
                    for w in range(Wx):
                        ay = shify-i+h
                        ax = shifx-j+w
                        by = shify+h
                        bx = shifx+w
                        f=False
                        if ((0<=ay<Ha and 0<=ax<Wa) and A[ay][ax]=="#"):
                            f=True
                            cnta+=1
                        if ((0<=by<Hb and 0<=bx<Wb) and B[by][bx]=="#"):
                            f=True
                            cntb+=1
                        if f:
                            board[h][w]="#"
                        else:
                            board[h][w]="."
                #if i==0 and j==4 and shifx==0 and shify==0:
                 #   print(board)
                
                if check(X, board, cnta, cntb):
                    #print(i,j,shify,shifx)
                    YES()
                    exit()
NO()