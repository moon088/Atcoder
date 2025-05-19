<<<<<<< HEAD
# E
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
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
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


N,M=MAP()
H=LIST()
g = [[] for _ in range(N)]

for i in range(M):
    u,v=MAP(); u-=1; v-=1
    if H[u]<=H[v]:
        g[v].append((u,0))
        g[u].append((v,abs(H[u]-H[v])))
    else:
        g[u].append((v,0))
        g[v].append((u,abs(H[u]-H[v])))



def dijkstra(n, g, i0=0):
    kk = 18
    mm = (1 << kk) - 1
    h = [(0,0)]
    D = [-1] * n
    visited = [0] * n
    D[i0] = 0
    while h:
        d, now = heappop(h)
        if visited[now]: continue
        visited[i] = 1
        for near, cost in g[now]:
            nd = d + cost
            if D[near] < 0 or D[near] > nd:
                if visited[near] == 0:
                    heappush(h, (near, nd))
                    D[near] = nd
    return D



D = dijkstra(N, g)
ans = -INF
for i in range(N):
    ans = max(ans, (H[0] - H[i]) - D[i])
=======
# E
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
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
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


N,M=MAP()
H=LIST()
g = [[] for _ in range(N)]

for i in range(M):
    u,v=MAP(); u-=1; v-=1
    if H[u]<=H[v]:
        g[v].append((u,0))
        g[u].append((v,abs(H[u]-H[v])))
    else:
        g[u].append((v,0))
        g[v].append((u,abs(H[u]-H[v])))



def dijkstra(n, g, i0=0):
    kk = 18
    mm = (1 << kk) - 1
    h = [(0,0)]
    D = [-1] * n
    visited = [0] * n
    D[i0] = 0
    while h:
        d, now = heappop(h)
        if visited[now]: continue
        visited[i] = 1
        for near, cost in g[now]:
            nd = d + cost
            if D[near] < 0 or D[near] > nd:
                if visited[near] == 0:
                    heappush(h, (near, nd))
                    D[near] = nd
    return D



D = dijkstra(N, g)
ans = -INF
for i in range(N):
    ans = max(ans, (H[0] - H[i]) - D[i])
>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(ans)