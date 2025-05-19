<<<<<<< HEAD
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

N=INT()
A=LIST()
Q=INT()
L,R=ZIP(Q)

acc = []
for i in range(N):
    if i==0:
        acc.append(0)
        continue
    if i%2==1:
        acc.append(acc[-1])
    else:
        acc.append(acc[-1]+A[i]-A[i-1])

#print(acc)

for i in range(Q):
    l,r = L[i],R[i]
    lidx = bisect(A, l)
    ridx = bisect(A, r)

    if lidx%2==0:
        sabunn = acc[lidx-1]+l-A[lidx-1]
       # print(sabunn)
    else:
        sabunn = acc[lidx-1]
       # print(sabunn)
    if ridx%2==0:
        migi = acc[ridx-1]+r-A[ridx-1]
       # print(migi)
    else:
        migi = acc[ridx-1]
    print(migi-sabunn)
=======
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

N=INT()
A=LIST()
Q=INT()
L,R=ZIP(Q)

acc = []
for i in range(N):
    if i==0:
        acc.append(0)
        continue
    if i%2==1:
        acc.append(acc[-1])
    else:
        acc.append(acc[-1]+A[i]-A[i-1])

#print(acc)

for i in range(Q):
    l,r = L[i],R[i]
    lidx = bisect(A, l)
    ridx = bisect(A, r)

    if lidx%2==0:
        sabunn = acc[lidx-1]+l-A[lidx-1]
       # print(sabunn)
    else:
        sabunn = acc[lidx-1]
       # print(sabunn)
    if ridx%2==0:
        migi = acc[ridx-1]+r-A[ridx-1]
       # print(migi)
    else:
        migi = acc[ridx-1]
    print(migi-sabunn)
>>>>>>> 5a60e3f (Sync local Atcoder directory)
    #print("gerg")