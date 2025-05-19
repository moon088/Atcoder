<<<<<<< HEAD
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

N,K,P=MAP()
L = []

for i in range(N):
    l = LIST()
    L.append([l[0], l[1:]])


t = list(product(range(P+1), repeat=K))
dp = [{i : INF for i in t} for _ in range(N+1)]


for i in range(N+1):
    for k, v in dp[i].items():
        if i==0 and k==(0,)*K:
            dp[0][k] = 0
        else:
            dp[i][k] = min(dp[i-1][k], dp[i][k])
        if i==N:
            continue
        newk = tuple(min(k[j]+L[i][1][j] ,P) for j in range(K))
        #print(newk)

        dp[i+1][newk] = min(dp[i+1][newk], dp[i][k]+L[i][0])

=======
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

N,K,P=MAP()
L = []

for i in range(N):
    l = LIST()
    L.append([l[0], l[1:]])


t = list(product(range(P+1), repeat=K))
dp = [{i : INF for i in t} for _ in range(N+1)]


for i in range(N+1):
    for k, v in dp[i].items():
        if i==0 and k==(0,)*K:
            dp[0][k] = 0
        else:
            dp[i][k] = min(dp[i-1][k], dp[i][k])
        if i==N:
            continue
        newk = tuple(min(k[j]+L[i][1][j] ,P) for j in range(K))
        #print(newk)

        dp[i+1][newk] = min(dp[i+1][newk], dp[i][k]+L[i][0])

>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(dp[-1][(P,)*K] if dp[-1][(P,)*K] <INF else -1)