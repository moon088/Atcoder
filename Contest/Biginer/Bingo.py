<<<<<<< HEAD
#C
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

N,T = MAP()
A=LIST()
board = [[0]*N for _ in range(N)]

def isBingo(i,j):
    if all(element==1 for element in board[i]):
        return True
    elif all(row[j] == 1 for row in board):
        return True
    elif i==j and all(board[i][i]==1 for i in range(N)):
        return True
    elif i+j ==N-1 and all(board[i][N-i-1]==1 for i in range(N)):
        return True
    else:
        return False
    
for i in range(T):
    x,y = (A[i]-1)%N, (A[i]-1)//N
    #print(x,y)
    board[y][x]=1
    if isBingo(y,x):
        print(i+1)
        exit()
print(-1)

=======
#C
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

N,T = MAP()
A=LIST()
board = [[0]*N for _ in range(N)]

def isBingo(i,j):
    if all(element==1 for element in board[i]):
        return True
    elif all(row[j] == 1 for row in board):
        return True
    elif i==j and all(board[i][i]==1 for i in range(N)):
        return True
    elif i+j ==N-1 and all(board[i][N-i-1]==1 for i in range(N)):
        return True
    else:
        return False
    
for i in range(T):
    x,y = (A[i]-1)%N, (A[i]-1)//N
    #print(x,y)
    board[y][x]=1
    if isBingo(y,x):
        print(i+1)
        exit()
print(-1)

>>>>>>> 5a60e3f (Sync local Atcoder directory)
