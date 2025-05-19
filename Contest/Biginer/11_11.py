<<<<<<< HEAD
# B
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

N=INT()
D=LIST()
ans=0
"""for i in range(N):
    ch_month = str(i+1)
    if len(ch_month)>=2 and not any(ch_month[i]==ch_month[i+1] for i in range(len(ch_month)-1)):
        continue
    month = int(ch_month[0])
   # print(month)
    day = D[i]
    temp=month
    cnt=0
    while temp<=day:
        cnt+=1
        temp+=month * 10**(cnt-1)
       # print(f"temp{temp}")
    if cnt!=0:
        ans+=cnt-1 
    #print(ans)
print(ans)"""


for m in range(N):
    for d in range(D[m]):
        s = str(m+1)+str(d+1)
        if  not all(s[i]== s[i+1] for i in range(len(s)-1)): 
            continue
        else:
          #  print(s)
            ans+=1
print(ans)
=======
# B
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

N=INT()
D=LIST()
ans=0
"""for i in range(N):
    ch_month = str(i+1)
    if len(ch_month)>=2 and not any(ch_month[i]==ch_month[i+1] for i in range(len(ch_month)-1)):
        continue
    month = int(ch_month[0])
   # print(month)
    day = D[i]
    temp=month
    cnt=0
    while temp<=day:
        cnt+=1
        temp+=month * 10**(cnt-1)
       # print(f"temp{temp}")
    if cnt!=0:
        ans+=cnt-1 
    #print(ans)
print(ans)"""


for m in range(N):
    for d in range(D[m]):
        s = str(m+1)+str(d+1)
        if  not all(s[i]== s[i+1] for i in range(len(s)-1)): 
            continue
        else:
          #  print(s)
            ans+=1
print(ans)
>>>>>>> 5a60e3f (Sync local Atcoder directory)
