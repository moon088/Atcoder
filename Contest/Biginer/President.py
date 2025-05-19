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
X,Y,Z=ZIP(N)
cost=[]
giseki = []
takahashi = 0
aoki = 0
for i in range(N):
    x,y=X[i],Y[i]
    if y-x>=0:
        cost.append((y-x)//2+1)
        giseki.append(Z[i])
        aoki += Z[i]
    else:
        takahashi += Z[i]
need = (takahashi+aoki)//2+1-takahashi
#print(takahashi, aoki, need)
#print(cost, giseki)

if takahashi>=need:
    print(0)
    exit()

dp = [[INF]*(need+1) for _ in range(len(cost)+1)]
dp[0][0]=0

for i in range(len(cost)+1):
    for j in range(need+1):
        if i==j==0:
            dp[i][j]=0
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        if i==len(cost):
            continue
        c,g = cost[i], giseki[i]  
        if j+g>=need:
            temp=need
        else:
            temp=j+g
        dp[i+1][temp] = min(dp[i+1][temp], dp[i][j]+c)
#print(dp)  
print(dp[-1][-1])

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
X,Y,Z=ZIP(N)
cost=[]
giseki = []
takahashi = 0
aoki = 0
for i in range(N):
    x,y=X[i],Y[i]
    if y-x>=0:
        cost.append((y-x)//2+1)
        giseki.append(Z[i])
        aoki += Z[i]
    else:
        takahashi += Z[i]
need = (takahashi+aoki)//2+1-takahashi
#print(takahashi, aoki, need)
#print(cost, giseki)

if takahashi>=need:
    print(0)
    exit()

dp = [[INF]*(need+1) for _ in range(len(cost)+1)]
dp[0][0]=0

for i in range(len(cost)+1):
    for j in range(need+1):
        if i==j==0:
            dp[i][j]=0
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        if i==len(cost):
            continue
        c,g = cost[i], giseki[i]  
        if j+g>=need:
            temp=need
        else:
            temp=j+g
        dp[i+1][temp] = min(dp[i+1][temp], dp[i][j]+c)
#print(dp)  
print(dp[-1][-1])

>>>>>>> 5a60e3f (Sync local Atcoder directory)
