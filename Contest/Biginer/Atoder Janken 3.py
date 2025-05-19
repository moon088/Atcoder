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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N=INT()
S=input()
dp = [[0]*3 for _ in range(N+1)]

for i in range(1,N+1):#i文字目のアクセスi-1idx
    for j in range(3): #0:グーR,1:チョキS,2:パーP
        aoki = S[i-1]
        if aoki=="R" and j==1:
            dp[i][j]=0
            continue
        elif aoki=="S" and j==2:
            dp[i][j]=0
            continue
        elif aoki=="P" and j==0:
            dp[i][j]=0
            continue
        
        if j==0:#グー出す
            if aoki=="R":#あいこ
                dp[i][j] = max(dp[i-1][1], dp[i-1][2])
            else:#かち
                dp[i][j] = max(dp[i-1][1], dp[i-1][2])+1
        elif j==1:
            if aoki=="S":
                dp[i][j] = max(dp[i-1][0], dp[i-1][2])
            else:
                dp[i][j] = max(dp[i-1][0], dp[i-1][2]) + 1
        else:
            if aoki =="P":
                dp[i][j] = max(dp[i-1][0], dp[i-1][1])
            else:
                dp[i][j] = max(dp[i-1][0], dp[i-1][1])+1
            
#print(dp)
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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N=INT()
S=input()
dp = [[0]*3 for _ in range(N+1)]

for i in range(1,N+1):#i文字目のアクセスi-1idx
    for j in range(3): #0:グーR,1:チョキS,2:パーP
        aoki = S[i-1]
        if aoki=="R" and j==1:
            dp[i][j]=0
            continue
        elif aoki=="S" and j==2:
            dp[i][j]=0
            continue
        elif aoki=="P" and j==0:
            dp[i][j]=0
            continue
        
        if j==0:#グー出す
            if aoki=="R":#あいこ
                dp[i][j] = max(dp[i-1][1], dp[i-1][2])
            else:#かち
                dp[i][j] = max(dp[i-1][1], dp[i-1][2])+1
        elif j==1:
            if aoki=="S":
                dp[i][j] = max(dp[i-1][0], dp[i-1][2])
            else:
                dp[i][j] = max(dp[i-1][0], dp[i-1][2]) + 1
        else:
            if aoki =="P":
                dp[i][j] = max(dp[i-1][0], dp[i-1][1])
            else:
                dp[i][j] = max(dp[i-1][0], dp[i-1][1])+1
            
#print(dp)
>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(max(dp[-1]))