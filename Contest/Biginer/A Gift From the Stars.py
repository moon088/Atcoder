<<<<<<< HEAD
# E
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
board = [set() for _ in range(N)]
for i in range(N-1):
    u,v=MAP(); u-=1; v-=1
    board[u].add(v); board[v].add(u)

deg=[0]*N
q = []
nelist = set()
for i in range(N):
    deg[i] = len(board[i])
    if deg[i]==1:
        ne = board[i].pop()
        board[i].add(ne)
        if ne not in nelist:
            nelist.add(ne)
            q.append(ne)

while q:
    now = q.pop()
    for near in board[now]:
        if deg[near]!=1:
            deg[near]=1
            for j in board[near]:
                if j==now:
                    continue
                board[j].remove(near)
                deg[j]-=1
                if deg[j]==1:
                    ne = board[j].pop()
                    board[j].add(ne)
                    if ne not in nelist:
                        nelist.add(ne)
                        q.append(ne)
                        
            board[near].clear()
            board[near].add(now)
#print(board)
ans=[]
for i in range(N):
    if deg[i]!=1:
        ans.append(deg[i])
ans.sort()
print(*ans)
    
=======
# E
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
board = [set() for _ in range(N)]
for i in range(N-1):
    u,v=MAP(); u-=1; v-=1
    board[u].add(v); board[v].add(u)

deg=[0]*N
q = []
nelist = set()
for i in range(N):
    deg[i] = len(board[i])
    if deg[i]==1:
        ne = board[i].pop()
        board[i].add(ne)
        if ne not in nelist:
            nelist.add(ne)
            q.append(ne)

while q:
    now = q.pop()
    for near in board[now]:
        if deg[near]!=1:
            deg[near]=1
            for j in board[near]:
                if j==now:
                    continue
                board[j].remove(near)
                deg[j]-=1
                if deg[j]==1:
                    ne = board[j].pop()
                    board[j].add(ne)
                    if ne not in nelist:
                        nelist.add(ne)
                        q.append(ne)
                        
            board[near].clear()
            board[near].add(now)
#print(board)
ans=[]
for i in range(N):
    if deg[i]!=1:
        ans.append(deg[i])
ans.sort()
print(*ans)
    
>>>>>>> 5a60e3f (Sync local Atcoder directory)
