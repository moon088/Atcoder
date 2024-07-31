# F
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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

def find_longest_path(graph):
    n = len(graph)
    indegree = [0] * n  # 各頂点の入次数
    for u in range(n):
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([v for v in range(n) if indegree[v] == 0])  # 入次数0の頂点
    dp = [0] * n 

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
            dp[v] = max(dp[v], dp[u] + 1)  # DP遷移

    return max(dp)  


N, M = MAP()
graph = [[] for _ in range(N)]
for _ in range(M):
    u,v = MAP()
    u-=1
    v-=1
    graph[u].append(v)

longest_path = find_longest_path(graph)
print(longest_path)
