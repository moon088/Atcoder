# D
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
from sortedcontainers import SortedSet, SortedList, SortedDict
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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

def prime_factorization(n):
    d = defaultdict(int)
    # 2で割り切れる限り割る
    while n % 2 == 0:
        d[2]+=1
        n //= 2
    # 3以上の奇数で割る
    i = 3
    while i * i <= n:
        while n % i == 0:
            d[i]+=1
            n //= i
        i += 2
    # 最後に残った数が1でなければ、それは素数
    if n > 1:
        d[n]+=1
    return d

K=INT()
ans = 1
factor = prime_factorization(K)

for i in factor:
    cnt = factor[i]
    num = i
    a,b = divmod(cnt , (num+1))    
    temp = num* (num*a+b)
    ans = max(ans, temp)
print(ans)
    
    
def min_N_for_factorial(factor, count):
    """ count 回素因数を含む N を求める """
    x = 0
    while count > 0:
        x += factor
        temp = x
        while temp % factor == 0:
            count -= 1
            temp //= factor
    return x

ans = 1
for prime, cnt in factor.items():
    ans = max(ans, min_N_for_factorial(prime, cnt))

print(ans)
