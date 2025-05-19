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
from sortedcontainers import SortedList
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


def make(y,x,size):
    #print(y,x,size+1)
    global ans
    flag = None
    for s in range(1,size+1):
        for near in [(y+s,x+s), (y+s,x-s), (y-s,x+s), (y-s,x-s)]:
            if C[near[0]][near[1]]!="#":
                if flag:
                    ans[flag]+=1
               # print(y,x,s,ans,0)
                return
        for near in [(y+s+1,x+s+1), (y+s+1,x-s-1), (y-s-1,x+s+1), (y-s-1,x-s-1)]:
            if not isInBoard(H,W,near[0], near[1]) or C[near[0]][near[1]]==".":
                flag = s
                break
    if flag:
        ans[flag]+=1
    #print(y,x,ans,1)
    return 
        
        

H,W=MAP()
C=BOARD(H)

ans = [0]*min(H,W)

for i in range(H):
    for j in range(W):
        if C[i][j]=="#":
            make(i,j,min(i,j,H-i-1,W-j-1))
print(*ans[1:]+[0])
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
from sortedcontainers import SortedList
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


def make(y,x,size):
    #print(y,x,size+1)
    global ans
    flag = None
    for s in range(1,size+1):
        for near in [(y+s,x+s), (y+s,x-s), (y-s,x+s), (y-s,x-s)]:
            if C[near[0]][near[1]]!="#":
                if flag:
                    ans[flag]+=1
               # print(y,x,s,ans,0)
                return
        for near in [(y+s+1,x+s+1), (y+s+1,x-s-1), (y-s-1,x+s+1), (y-s-1,x-s-1)]:
            if not isInBoard(H,W,near[0], near[1]) or C[near[0]][near[1]]==".":
                flag = s
                break
    if flag:
        ans[flag]+=1
    #print(y,x,ans,1)
    return 
        
        

H,W=MAP()
C=BOARD(H)

ans = [0]*min(H,W)

for i in range(H):
    for j in range(W):
        if C[i][j]=="#":
            make(i,j,min(i,j,H-i-1,W-j-1))
print(*ans[1:]+[0])
>>>>>>> 5a60e3f (Sync local Atcoder directory)
