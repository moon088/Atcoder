<<<<<<< HEAD
# E
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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N = INT()
E = [[] for _ in range(N)]
for i in range(N-1):
    a,b,c = MAP()
    a-=1
    b-=1
    E[a].append((b,c))
    E[b].append((a,c))    

def search_far_node(s):
    dis = [INF for _ in range(N)]
    dis[s]=0
    q = deque()
    q.append(s)
    #print(E)
    while q:
        #print(q)
        v = q.popleft()

        for near, cost in E[v]:
            if dis[v]+cost < dis[near]:
                dis[near] = dis[v]+cost
                q.append(near)
    #print(dis)
    V = -INF
    C = -INF
    for idx,c in enumerate(dis):
        if c >C:
            C = c 
            V = idx 
    #print(V,C)
    return V,C

V,C = search_far_node(0)
_, result = search_far_node(V)   

total = 0
for i in E:
    for j in i:
        total += j[1]

    
ans = total-result
=======
# E
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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N = INT()
E = [[] for _ in range(N)]
for i in range(N-1):
    a,b,c = MAP()
    a-=1
    b-=1
    E[a].append((b,c))
    E[b].append((a,c))    

def search_far_node(s):
    dis = [INF for _ in range(N)]
    dis[s]=0
    q = deque()
    q.append(s)
    #print(E)
    while q:
        #print(q)
        v = q.popleft()

        for near, cost in E[v]:
            if dis[v]+cost < dis[near]:
                dis[near] = dis[v]+cost
                q.append(near)
    #print(dis)
    V = -INF
    C = -INF
    for idx,c in enumerate(dis):
        if c >C:
            C = c 
            V = idx 
    #print(V,C)
    return V,C

V,C = search_far_node(0)
_, result = search_far_node(V)   

total = 0
for i in E:
    for j in i:
        total += j[1]

    
ans = total-result
>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(ans)