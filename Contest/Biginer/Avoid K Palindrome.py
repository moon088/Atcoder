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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60
MOD = 998244353

#方針:= 1.部分文字列Kを左端で作り、回文でないものを辞書に追加していく。この時2^K(すべて？)で計算量かかる。
#2.辞書に追加されたものをひとつづつ取り出し、長さKを超えていたら一文字追加し、先頭削除して回文でないものをまた辞書に入れていく。
#3.辞書に入っているものを全て足したものを答えに入れる。
#最終的にオーダーは2^K * K(これは回文判定) * N(文字列をずらす回数)

#結局やってることは、最初のK文字全探索で回文でない文字列を全パターン列挙してそれぞれに対して一文字ずつずらして加算していく

N, K = map(int, input().split())
S = input()

def make_initial_kdict(S,l):
    d = {"":1}
    for s in S:
        new_d = dict()#更新用
        for k,v in d.items():
            for i in ["A", "B"]:
                if s==i or s=="?":#A,Bなら片方、?なら両方実施
                    new_k = f"{k}{i}"
                    #print(new_k)
                    if len(new_k)>l:
                        new_k=new_k[-l:]
                    if len(new_k)==l and new_k==new_k[::-1]:
                        continue
    
                    if new_k in new_d:
                        new_d[new_k] += v
                        new_d[new_k] %= MOD
                    else:
                        new_d[new_k] = v
        d = new_d
        #print(d)
    ans=0
    for i in d:
        ans+=d[i]
        ans %= MOD
    return ans
result = make_initial_kdict(S,K)
print(result)
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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60
MOD = 998244353

#方針:= 1.部分文字列Kを左端で作り、回文でないものを辞書に追加していく。この時2^K(すべて？)で計算量かかる。
#2.辞書に追加されたものをひとつづつ取り出し、長さKを超えていたら一文字追加し、先頭削除して回文でないものをまた辞書に入れていく。
#3.辞書に入っているものを全て足したものを答えに入れる。
#最終的にオーダーは2^K * K(これは回文判定) * N(文字列をずらす回数)

#結局やってることは、最初のK文字全探索で回文でない文字列を全パターン列挙してそれぞれに対して一文字ずつずらして加算していく

N, K = map(int, input().split())
S = input()

def make_initial_kdict(S,l):
    d = {"":1}
    for s in S:
        new_d = dict()#更新用
        for k,v in d.items():
            for i in ["A", "B"]:
                if s==i or s=="?":#A,Bなら片方、?なら両方実施
                    new_k = f"{k}{i}"
                    #print(new_k)
                    if len(new_k)>l:
                        new_k=new_k[-l:]
                    if len(new_k)==l and new_k==new_k[::-1]:
                        continue
    
                    if new_k in new_d:
                        new_d[new_k] += v
                        new_d[new_k] %= MOD
                    else:
                        new_d[new_k] = v
        d = new_d
        #print(d)
    ans=0
    for i in d:
        ans+=d[i]
        ans %= MOD
    return ans
result = make_initial_kdict(S,K)
print(result)
>>>>>>> 5a60e3f (Sync local Atcoder directory)
