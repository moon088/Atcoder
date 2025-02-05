# D
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


def bfs(graph, start):
    dist = {start: 0}
    que = deque([start])

    while que:
        state = que.popleft()
        for v in range(9):
            if v not in state:
                emp_v = v
                break

        for frm_v in graph[emp_v]:
            nxt_state = list(state)

            for i in range(8):
                if nxt_state[i] == frm_v:
                    nxt_state[i] = emp_v
            nxt_state = tuple(nxt_state)
            if nxt_state not in dist:
                dist[nxt_state] = dist[state] + 1
                que.append(nxt_state)
    return dist


m = INT()
edges = [LIST() for i in range(m)]
p = LIST()
n = 9

graph = [[] for i in range(n)]
for u, v in edges:
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


start = tuple([val - 1 for val in p])

dist = bfs(graph, start)
ans = tuple([i for i in range(8)])

if ans in dist:
    print(dist[ans])
else:
    print(-1)