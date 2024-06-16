#bitの走査あれこれ
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

#２進数でbitがたっている個数-1(組み込み使用)
#これpython3.9以前(３．１０～はちょっと違うコーディング)
def count_set_bits(n):
    return bin(n).count('1')

#２進数でbitがたっている個数-2(ちゃんと数える)
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

#2進数を求める関数(先頭に"0b"つくのに注意)
def to_binary(n):
    return bin(n)[2:]

#２進数に変換し、下桁から配列に格納
def cnv_bin_array(n):
    n_bin = [0]*60
    for i in range(60):
        if n & 1 << i:
            n_bin[i] = 1
    return n_bin


#2進数の各桁が配列に格納されているものを１０進数へ変換
def binary_array_to_decimal(binary_array):
    binary_string = ''.join(map(str, binary_array))
    decimal_value = int(binary_string, 2)
    return decimal_value