#C
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
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

def get_input():
    return sys.stdin.readline().rstrip()

def count_valid_combinations(N, M, K, tests):
    valid_count = 0

    # 2^N通りの鍵の状態をビット全探索
    for mask in range(1 << N):
        valid = True
        for keys, result in tests:
            correct_keys = sum(1 for key in keys if mask & (1 << (key - 1)))
            if (result == 'o' and correct_keys < K) or (result == 'x' and correct_keys >= K):
                valid = False
                break
        if valid:
            valid_count += 1

    return valid_count

# 入力処理
"""
N, M, K = map(int, get_input().split())
tests = []
for _ in range(M):
    res = get_input().split()
    C = int(res[0])
    A = list(map(int, res[1:C+1]))
    R = res[-1]
    tests.append((A, R))

# 結果の表示
"""
N,M,K=MAP()
C=[]
tests=[]
for i in range(M):
    c,*a,r=MIXED_LIST()
    C.append(c)
    tests.append((a,r))
print(count_valid_combinations(N, M, K, tests))
