<<<<<<< HEAD
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

# ... (他の import 文などは省略) ...

def main():
    N, M = MAP()
    graph = [[] for _ in range(N)]
    U = []
    V = []
    W = []
    for i in range(M):
        u, v, w = MAP()
        u -= 1  # 0-indexed に変換
        v -= 1
        U.append(u)
        V.append(v)
        W.append(w)

    # Bellman-Ford 法の初期設定
    dist = [INF] * N  # 各頂点への仮の距離を INF で初期化
    # 問題文の条件から、特定の始点や終点は指定されていないため、
    # 全ての頂点を始点として Bellman-Ford 法を適用する必要がある
    
    # 負の閉路が存在するかどうかのフラグ
    has_negative_cycle = False

    # 全ての頂点を始点として Bellman-Ford 法を適用
    for start in range(N):
        dist = [INF] * N 
        dist[start] = 0  # 始点の距離は 0

        # N-1 回の緩和操作
        for loop in range(N - 1):
            for i in range(M):
                if dist[U[i]] == INF:
                    continue  # 到達不可能な頂点からの緩和はスキップ

                if dist[V[i]] > dist[U[i]] + W[i]:
                    dist[V[i]] = dist[U[i]] + W[i]  # 緩和操作

        # もう 1 回緩和操作を行い、負の閉路を検出
        for i in range(M):
            if dist[U[i]] == INF:
                continue

            if dist[V[i]] > dist[U[i]] + W[i]:
                has_negative_cycle = True  # 負の閉路を検出
                break  # 負の閉路が存在すれば即座にループを抜ける
        
        if has_negative_cycle:
            break  # 負の閉路が存在すれば、それ以降の探索は不要

    if has_negative_cycle:
        print("inf")  # 負の閉路が存在する場合は "inf" を出力
    else:
        # 問題の条件「y_u - y_v = w」を満たすように y_i を計算
        # y_0 を 0 とすると、他の y_i は dist[i] で表せる
        for i in range(N):
            print(dist[i], end=" ") 

if __name__ == "__main__":
=======
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

# ... (他の import 文などは省略) ...

def main():
    N, M = MAP()
    graph = [[] for _ in range(N)]
    U = []
    V = []
    W = []
    for i in range(M):
        u, v, w = MAP()
        u -= 1  # 0-indexed に変換
        v -= 1
        U.append(u)
        V.append(v)
        W.append(w)

    # Bellman-Ford 法の初期設定
    dist = [INF] * N  # 各頂点への仮の距離を INF で初期化
    # 問題文の条件から、特定の始点や終点は指定されていないため、
    # 全ての頂点を始点として Bellman-Ford 法を適用する必要がある
    
    # 負の閉路が存在するかどうかのフラグ
    has_negative_cycle = False

    # 全ての頂点を始点として Bellman-Ford 法を適用
    for start in range(N):
        dist = [INF] * N 
        dist[start] = 0  # 始点の距離は 0

        # N-1 回の緩和操作
        for loop in range(N - 1):
            for i in range(M):
                if dist[U[i]] == INF:
                    continue  # 到達不可能な頂点からの緩和はスキップ

                if dist[V[i]] > dist[U[i]] + W[i]:
                    dist[V[i]] = dist[U[i]] + W[i]  # 緩和操作

        # もう 1 回緩和操作を行い、負の閉路を検出
        for i in range(M):
            if dist[U[i]] == INF:
                continue

            if dist[V[i]] > dist[U[i]] + W[i]:
                has_negative_cycle = True  # 負の閉路を検出
                break  # 負の閉路が存在すれば即座にループを抜ける
        
        if has_negative_cycle:
            break  # 負の閉路が存在すれば、それ以降の探索は不要

    if has_negative_cycle:
        print("inf")  # 負の閉路が存在する場合は "inf" を出力
    else:
        # 問題の条件「y_u - y_v = w」を満たすように y_i を計算
        # y_0 を 0 とすると、他の y_i は dist[i] で表せる
        for i in range(N):
            print(dist[i], end=" ") 

if __name__ == "__main__":
>>>>>>> 5a60e3f (Sync local Atcoder directory)
    main()