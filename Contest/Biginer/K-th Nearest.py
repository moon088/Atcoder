<<<<<<< HEAD
# D
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

N,Q=MAP()
A=LIST()
A.sort()
#print(A)
ans=[]
def decide_d(A,b,k):
    left = 0
    right =10**9
    
    
    while left<right:
        mid = (right+left)//2
        mini_idx = bisect_left(A, b-mid)
        maxi_idx = bisect(A, b+mid)
        #print(mini_idx,maxi_idx)
        if maxi_idx-mini_idx >= k:
            right=mid
        else:
            left=mid+1
    #print(mini_idx,maxi_idx)
    #ans = max(b-A[mini_idx], A[maxi_idx]-b)
    ans.append(right)
    return

for i in range(Q):
    b,k=MAP()
    decide_d(A,b,k)
for i in ans:
    print(i)
        
=======
# D
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

N,Q=MAP()
A=LIST()
A.sort()
#print(A)
ans=[]
def decide_d(A,b,k):
    left = 0
    right =10**9
    
    
    while left<right:
        mid = (right+left)//2
        mini_idx = bisect_left(A, b-mid)
        maxi_idx = bisect(A, b+mid)
        #print(mini_idx,maxi_idx)
        if maxi_idx-mini_idx >= k:
            right=mid
        else:
            left=mid+1
    #print(mini_idx,maxi_idx)
    #ans = max(b-A[mini_idx], A[maxi_idx]-b)
    ans.append(right)
    return

for i in range(Q):
    b,k=MAP()
    decide_d(A,b,k)
for i in ans:
    print(i)
        
>>>>>>> 5a60e3f (Sync local Atcoder directory)
        