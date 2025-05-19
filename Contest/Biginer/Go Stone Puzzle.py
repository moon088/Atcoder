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

N=INT()
S=list_input()
T=list_input()

if S.count("W") != T.count("W"):
    print(-1)
    exit()
    
S.append(".")
T.append(".")
S.append(".")
T.append(".")

dp = {}
dp["".join(S)]=0
d = deque()
d.append(S)

while d:
    S = d.popleft()
    
    a=S.index(".")

    for i in range(N+1):
        x = S[i]
        y = S[i+1]
        if x!="." and y!=".":
            temp=S[:]
            temp[i]="."
            temp[i+1]="."
            temp[a]=x
            temp[a+1]=y

            if "".join(temp) not in dp or dp["".join(S)]+1< dp["".join(temp)]:
                dp["".join(temp)] = dp["".join(S)] + 1
                d.append(temp)
        #print(dp)


if "".join(T) in dp:
    print(dp["".join(T)])
else:
    print(-1)
    
    
    
    
    
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

N=INT()
S=list_input()
T=list_input()

if S.count("W") != T.count("W"):
    print(-1)
    exit()
    
S.append(".")
T.append(".")
S.append(".")
T.append(".")

dp = {}
dp["".join(S)]=0
d = deque()
d.append(S)

while d:
    S = d.popleft()
    
    a=S.index(".")

    for i in range(N+1):
        x = S[i]
        y = S[i+1]
        if x!="." and y!=".":
            temp=S[:]
            temp[i]="."
            temp[i+1]="."
            temp[a]=x
            temp[a+1]=y

            if "".join(temp) not in dp or dp["".join(S)]+1< dp["".join(temp)]:
                dp["".join(temp)] = dp["".join(S)] + 1
                d.append(temp)
        #print(dp)


if "".join(T) in dp:
    print(dp["".join(T)])
else:
    print(-1)
    
    
    
    
    
>>>>>>> 5a60e3f (Sync local Atcoder directory)
    