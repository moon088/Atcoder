# E
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
def isInBoard(H,W,y,x): return 0<=y<H and 0<=x<W
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

#半分全列挙する
#半分のグループに対して,2^(N/2)の全探索してmemo[i][j]:=i個選んだ合計値として2分探索
N,K,P = MAP()
A= LIST()
A.sort()
half = N//2
sub1 = [[] for _ in range(half+1)]
sub2 = [[] for _ in range(N-half+1)]
s1 = A[:half]; s2 = A[half:]

for bit in range(1<<half):
    temp = 0
    kosuu = 0
    for j in range(half):
        if bit>>j & 1:
            temp += A[j]
            kosuu += 1
    sub1[kosuu].append(temp)

for bit in range(1<<(N-half)):
    temp = 0
    kosuu = 0
    for j in range(N-half):
        if bit>>j & 1:
            temp += A[half+j]
            kosuu += 1
    sub2[kosuu].append(temp)
            
ans = 0
for ko, i in enumerate(sub1):
    if ko>K:
        break
    idx = K-ko
    if idx>=len(sub2):
        continue
    for j in sub1[ko]:
        if j>P:
            break
        idx = K-ko
        #print(i,ko,j,idx)
        ans += bisect(sub2[idx], P-j)
print(ans)