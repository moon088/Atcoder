<<<<<<< HEAD
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

A=[LIST() for _ in range(9)]

for i in range(9):
    c = [False]*9
    for j in range(9):
        c[A[i][j]-1]=True
    if all(c):
        continue
    else:
        NO()
        exit()

for i in range(9):
    c = [False]*9
    for j in range(9):
        c[A[j][i]-1]=True
    if all(c):
        continue
    else:
        NO()
        exit()

c=[[False]*9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        i_quo, i_remain = divmod(i, 3)
        j_quo, j_remain = divmod(j, 3)
        num = i_quo*3+j_quo
        c[num][A[i][j]-1] = True

for i in range(9):
    if all(c[i]):
        continue
    else:
        NO()
        exit()
=======
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

A=[LIST() for _ in range(9)]

for i in range(9):
    c = [False]*9
    for j in range(9):
        c[A[i][j]-1]=True
    if all(c):
        continue
    else:
        NO()
        exit()

for i in range(9):
    c = [False]*9
    for j in range(9):
        c[A[j][i]-1]=True
    if all(c):
        continue
    else:
        NO()
        exit()

c=[[False]*9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        i_quo, i_remain = divmod(i, 3)
        j_quo, j_remain = divmod(j, 3)
        num = i_quo*3+j_quo
        c[num][A[i][j]-1] = True

for i in range(9):
    if all(c[i]):
        continue
    else:
        NO()
        exit()
>>>>>>> 5a60e3f (Sync local Atcoder directory)
YES()