<<<<<<< HEAD
#E
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
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

H,W,N = MAP()
board = BOARD(H)

def move(sy,sx,gy,gx):
    dis = [[INF]*W for _ in range(H)]
    dis[sy][sx]=0
    queue = [(0,sy,sx)]
    while queue:
        cur_dis,y,x = heappop(queue)
        
        for dy,dx in dxy:
            if 0<= dy+y <H and 0<= dx+x <W and board[dy+y][dx+x]!="X":
                near_dis = cur_dis+1
                if near_dis < dis[dy+y][dx+x]:
                    dis[dy+y][dx+x]=near_dis
                    heappush(queue, (near_dis,dy+y,dx+x))
    return dis[gy][gx]

cource=[None]*(N+1)
for i in range(H):
    for j in range(W):
        if "0"<=board[i][j]<="9":
            cource[int(board[i][j])]=(i,j) 
        if board[i][j]=="S":
            cource[0]=(i,j)
            
out=0
for i in range(N):
    out+=move(cource[i][0],cource[i][1],cource[i+1][0],cource[i+1][1])
print(out)
                
    

=======
#E
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
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

H,W,N = MAP()
board = BOARD(H)

def move(sy,sx,gy,gx):
    dis = [[INF]*W for _ in range(H)]
    dis[sy][sx]=0
    queue = [(0,sy,sx)]
    while queue:
        cur_dis,y,x = heappop(queue)
        
        for dy,dx in dxy:
            if 0<= dy+y <H and 0<= dx+x <W and board[dy+y][dx+x]!="X":
                near_dis = cur_dis+1
                if near_dis < dis[dy+y][dx+x]:
                    dis[dy+y][dx+x]=near_dis
                    heappush(queue, (near_dis,dy+y,dx+x))
    return dis[gy][gx]

cource=[None]*(N+1)
for i in range(H):
    for j in range(W):
        if "0"<=board[i][j]<="9":
            cource[int(board[i][j])]=(i,j) 
        if board[i][j]=="S":
            cource[0]=(i,j)
            
out=0
for i in range(N):
    out+=move(cource[i][0],cource[i][1],cource[i+1][0],cource[i+1][1])
print(out)
                
    

>>>>>>> 5a60e3f (Sync local Atcoder directory)
