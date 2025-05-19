"""# E
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd, prod
from cmath import phase
from itertools import accumulate, chain, combinations, combinations_with_replacement, permutations, compress, dropwhile, takewhile, groupby, product, starmap
from functools import cmp_to_key,lru_cache
from operator import itemgetter, mul, xor
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush , heappop
from functools import reduce, lru_cache
from sortedcontainers import SortedSet, SortedList, SortedDict
from decimal import Decimal, ROUND_HALF_UP
from more_itertools import run_length
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
def ROUND_OFF(X,k): return  (X // (10 ** k) + 5) // 10 * 10 ** (k + 1)
def YES(): return print("Yes")
def NO(): return print("No")
alph = 'abcdefghijklmnopqrstuvwxyz'
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


N,D=MAP()
A=LIST()

mod_query = [defaultdict(int) for _ in range(D)]
max_idx   = [-1] * D
if D==0:
    d = defaultdict(int)
    for i in range(N):
        d[A[i]]+=1
    ans=0
    for i in d:
        ans+=d[i]-1
    print(ans)
    exit()
    
for x in A:
    m = x % D
    k = x // D
    mod_query[m][k] += 1
    max_idx[m] = max(max_idx[m], k)

ans = 0
for m in range(D):
    if max_idx[m] < 0:
        continue
    dp1 = 0
    dp2 = 0
    for now in range(max_idx[m], -1, -1):
        cnt = mod_query[m].get(now, 0)
        curr = cnt + min(dp1, dp2)
        dp2, dp1 = dp1, curr
    ans += min(dp1, dp2)

print(ans)"""
# D
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd, prod
from cmath import phase
from itertools import accumulate, chain, combinations, combinations_with_replacement, permutations, compress, dropwhile, takewhile, groupby, product, starmap
from functools import cmp_to_key,lru_cache
from operator import itemgetter, mul, xor
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush , heappop
from functools import reduce, lru_cache
from sortedcontainers import SortedSet, SortedList, SortedDict
from decimal import Decimal, ROUND_HALF_UP
from more_itertools import run_length
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
def ROUND_OFF(X,k): return  (X // (10 ** k) + 5) // 10 * 10 ** (k + 1)
def YES(): return print("Yes")
def NO(): return print("No")
alph = 'abcdefghijklmnopqrstuvwxyz'
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


N,D=MAP()
A=LIST()


@lru_cache(maxsize=None)
def cal_cost(mod, now):
    if now >= max_idx[mod]-1:
        return mod_query[mod][now]
    return min(cal_cost(mod, now+1)+mod_query[mod][now], cal_cost(mod, now+2)+mod_query[mod][now])
    
if D==0:
    d=defaultdict(int)
    ans=0
    for i in range(N):
        d[A[i]]+=1
    for i in d:
        ans += d[i]-1    
    print(ans)
    exit()

mod_query = [defaultdict(int) for _ in range(D)]
max_idx = [-1]*D
for i in range(N):
    mod_query[A[i]%D][A[i]//D]+=1 
    max_idx[A[i]%D] = max(max_idx[A[i]%D], A[i]//D)
#print(mod_query, max_idx)


ans = 0
for q in range(D):
    temp = 0
    q_ans = min(cal_cost(q, 0), cal_cost(q, 1))
    ans += q_ans
    cal_cost.cache_clear()
   # print(q_ans)
print(ans)