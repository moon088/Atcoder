<<<<<<< HEAD
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

def find_good_permutation(N, M, A):
    # Aをセットにして要素の存在を高速にチェックできるようにする
    A_set = set(A)

    # 結果の順列を格納するリスト
    P = []

    # 辞書順で最小の順列を構築する
    for i in range(1, N + 1):
        # まずは、Aのいずれの要素とも一致しない部分列を作成する
        if i not in A_set:
            P.append(i)

    # Aの要素を追加するが、これは辞書順を保ったまま
    for a in A:
        P.append(a)

    return P


N,M=MAP()
A = LIST()

# 良い順列を求める
result = find_good_permutation(N, M, A)

# 結果の出力
print(" ".join(map(str, result)))
=======
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

def find_good_permutation(N, M, A):
    # Aをセットにして要素の存在を高速にチェックできるようにする
    A_set = set(A)

    # 結果の順列を格納するリスト
    P = []

    # 辞書順で最小の順列を構築する
    for i in range(1, N + 1):
        # まずは、Aのいずれの要素とも一致しない部分列を作成する
        if i not in A_set:
            P.append(i)

    # Aの要素を追加するが、これは辞書順を保ったまま
    for a in A:
        P.append(a)

    return P


N,M=MAP()
A = LIST()

# 良い順列を求める
result = find_good_permutation(N, M, A)

# 結果の出力
print(" ".join(map(str, result)))
>>>>>>> 5a60e3f (Sync local Atcoder directory)
