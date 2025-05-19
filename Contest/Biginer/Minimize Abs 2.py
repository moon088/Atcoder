<<<<<<< HEAD
# C
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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def BOARD_INT(H): return [list(map(int, input().split())) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

D=INT()
#x = 0,1,2,4,9,16,25,36,49,64,81,,,,2*10^6
x = [i**2 for i in range(2*10**6)]
y = [i**2 for i in range(2*10**6)]
ans = INF
for i in x:
    v = i-D
    if v>=0:
        idx = 0
    else:
        idx = bisect_left(y,-v)
        
    if idx ==0 and ans>=abs(y[idx]+v):
        memo = [i,idx,v,y[idx]]
        ans = min(ans, abs(y[idx]+v))
       # print(memo)
    elif ans >=abs(y[idx]+v) or ans>= abs(y[idx-1]+v):
        memo = [i,idx,v,y[idx]]
       # print(memo)
        ans = min(ans, abs(y[idx]+v), abs((y[idx-1]+v)))

    
print(ans)
=======
# C
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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
def BOARD_INT(H): return [list(map(int, input().split())) for _ in range(H)]
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

D=INT()
#x = 0,1,2,4,9,16,25,36,49,64,81,,,,2*10^6
x = [i**2 for i in range(2*10**6)]
y = [i**2 for i in range(2*10**6)]
ans = INF
for i in x:
    v = i-D
    if v>=0:
        idx = 0
    else:
        idx = bisect_left(y,-v)
        
    if idx ==0 and ans>=abs(y[idx]+v):
        memo = [i,idx,v,y[idx]]
        ans = min(ans, abs(y[idx]+v))
       # print(memo)
    elif ans >=abs(y[idx]+v) or ans>= abs(y[idx-1]+v):
        memo = [i,idx,v,y[idx]]
       # print(memo)
        ans = min(ans, abs(y[idx]+v), abs((y[idx-1]+v)))

    
print(ans)
>>>>>>> 5a60e3f (Sync local Atcoder directory)
    