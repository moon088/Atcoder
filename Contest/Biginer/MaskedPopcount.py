<<<<<<< HEAD
#D
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
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N,M =MAP()
MOD=998244353
ans = 0
# bit毎に独立してカウント
for i in range(60):
    if M >> i & 1:
        # 0以上 N以下で iビット目が1となる整数の個数を数える
        up = N >> (i+1)
        base = 1 << i
        ans += (up * base) % MOD
        ans %= MOD
        if N >> i & 1:
            ans += (N % base) + 1
            ans %= MOD

print(ans)
=======
#D
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
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N,M =MAP()
MOD=998244353
ans = 0
# bit毎に独立してカウント
for i in range(60):
    if M >> i & 1:
        # 0以上 N以下で iビット目が1となる整数の個数を数える
        up = N >> (i+1)
        base = 1 << i
        ans += (up * base) % MOD
        ans %= MOD
        if N >> i & 1:
            ans += (N % base) + 1
            ans %= MOD

print(ans)
>>>>>>> 5a60e3f (Sync local Atcoder directory)
