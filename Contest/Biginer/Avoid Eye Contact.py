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

H,W=MAP()
board=BOARD(H)

def make(i,j,kigou):
    if kigou==">":
        idx = 2    
    elif kigou=="<":
        idx = 3
    elif kigou=="^":
        idx = 1
    else:
        idx = 0

    i += Dxy[idx][0]
    j += Dxy[idx][1]
    while 0<=i<H and 0<=j<W:
        if board[i][j]=="." or board[i][j]=="/":
            board[i][j]="/"
        else:
            break
        i+=Dxy[idx][0]
        j+=Dxy[idx][1]

hito = ("<", ">", "^", "v")
for i in range(H):
    for j in range(W):
        if board[i][j] in hito:
            make(i,j,board[i][j])
        elif board[i][j]=="S":
            s=(i,j)
        elif board[i][j]=="G":
            g=(i,j)
#print(board)
    
    
q = deque([s]) 
memo = [[INF]*W for _ in range(H)]
memo[s[0]][s[1]] = 0
while q:
    i, j = q.popleft() 
    if i==g[0] and j==g[1]:
        print(memo[g[0]][g[1]])
        exit()
    for d in Dxy:
        ni, nj = i+d[0], j+d[1]
        if 0 <= ni < H and 0 <= nj < W:
            if board[ni][nj] == "#" or board[ni][nj]=="/" or board[ni][nj] in hito: continue  
            if memo[ni][nj] > memo[i][j]+1:          
                memo[ni][nj] = memo[i][j]+1
                q.append((ni, nj))
print(-1)
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

H,W=MAP()
board=BOARD(H)

def make(i,j,kigou):
    if kigou==">":
        idx = 2    
    elif kigou=="<":
        idx = 3
    elif kigou=="^":
        idx = 1
    else:
        idx = 0

    i += Dxy[idx][0]
    j += Dxy[idx][1]
    while 0<=i<H and 0<=j<W:
        if board[i][j]=="." or board[i][j]=="/":
            board[i][j]="/"
        else:
            break
        i+=Dxy[idx][0]
        j+=Dxy[idx][1]

hito = ("<", ">", "^", "v")
for i in range(H):
    for j in range(W):
        if board[i][j] in hito:
            make(i,j,board[i][j])
        elif board[i][j]=="S":
            s=(i,j)
        elif board[i][j]=="G":
            g=(i,j)
#print(board)
    
    
q = deque([s]) 
memo = [[INF]*W for _ in range(H)]
memo[s[0]][s[1]] = 0
while q:
    i, j = q.popleft() 
    if i==g[0] and j==g[1]:
        print(memo[g[0]][g[1]])
        exit()
    for d in Dxy:
        ni, nj = i+d[0], j+d[1]
        if 0 <= ni < H and 0 <= nj < W:
            if board[ni][nj] == "#" or board[ni][nj]=="/" or board[ni][nj] in hito: continue  
            if memo[ni][nj] > memo[i][j]+1:          
                memo[ni][nj] = memo[i][j]+1
                q.append((ni, nj))
print(-1)
>>>>>>> 5a60e3f (Sync local Atcoder directory)
