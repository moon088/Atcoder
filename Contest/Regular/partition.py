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

N,K = MAP()
A=LIST()

if K>0: 
    print("Yes")
    A.sort()
    for i in A:
        print(i, end=" ")
    exit()


else:
    #K以上を常に維持して累積和をとれるか？
    A.sort(reverse=True)
    sum=0
    for i in A:
        sum+=i
        if sum<K:
            print("No")
            exit()
    print("Yes")
    for i in A:
        print(i,end=" ")
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

N,K = MAP()
A=LIST()

if K>0: 
    print("Yes")
    A.sort()
    for i in A:
        print(i, end=" ")
    exit()


else:
    #K以上を常に維持して累積和をとれるか？
    A.sort(reverse=True)
    sum=0
    for i in A:
        sum+=i
        if sum<K:
            print("No")
            exit()
    print("Yes")
    for i in A:
        print(i,end=" ")
>>>>>>> 5a60e3f (Sync local Atcoder directory)
    