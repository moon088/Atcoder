<<<<<<< HEAD
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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N=INT()
S=list(input().strip())
Q=INT()
T,X,C=[],[],[]
for i in range(Q):
    t,x,c=input().split()
    T.append(int(t))
    X.append(int(x)-1)
    C.append(c)

flag=None
idx=N
moji = []
for i in range(Q-1,-1,-1):
    if flag==None and (T[i]==2 or T[i]==3):
        flag = T[i]
        idx = i
    elif T[i]==1:
        moji.append((X[i],C[i],i))
        
#print(moji,flag,idx)

if flag==2:
    S = [S[i].lower() for i in range(N)]
elif flag==3:
    S = [S[i].upper() for i in range(N)]
#print(S)
while moji:
    x,c,i = moji.pop()
    #print(moji)
    if i<idx:
        if flag==2:
            S[x] = c.lower()
        elif flag==3:
            S[x] = c.upper()
        else:
            S[x]=c
    else:
        S[x] = c

for i in S:
    print(i,end="")
=======
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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N=INT()
S=list(input().strip())
Q=INT()
T,X,C=[],[],[]
for i in range(Q):
    t,x,c=input().split()
    T.append(int(t))
    X.append(int(x)-1)
    C.append(c)

flag=None
idx=N
moji = []
for i in range(Q-1,-1,-1):
    if flag==None and (T[i]==2 or T[i]==3):
        flag = T[i]
        idx = i
    elif T[i]==1:
        moji.append((X[i],C[i],i))
        
#print(moji,flag,idx)

if flag==2:
    S = [S[i].lower() for i in range(N)]
elif flag==3:
    S = [S[i].upper() for i in range(N)]
#print(S)
while moji:
    x,c,i = moji.pop()
    #print(moji)
    if i<idx:
        if flag==2:
            S[x] = c.lower()
        elif flag==3:
            S[x] = c.upper()
        else:
            S[x]=c
    else:
        S[x] = c

for i in S:
    print(i,end="")
>>>>>>> 5a60e3f (Sync local Atcoder directory)
    