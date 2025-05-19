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


"""
愚直だとオーダー(N^3)でだめ、各座標ごとの外堀を出してその外堀ごとの回転回数をmod4で計算する方針
def out_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end="")
        print()



def make_rotate(board, s, g):
    temp = [board[i][s:g+1] for i in range(s, g+1)]
   # print("temp")
    #out_board(temp)
    transposed = list(zip(*temp))
    rotated = [list(reversed(row)) for row in transposed]
    #print("rotated")
    #out_board(rotated)
    
    for i in range(s, g+1):
        for j in range(s, g+1):
            board[i][j] = rotated[i-s][j-s]
    #print("newboard")
   # out_board(board)
    return board

for i in range(1, N//2+1):
    board = make_rotate(board, i-1, N-i)
out_board(board)"""


N=INT()
board = []
for i in range(N):
    b = list(input())
    board.append(b)
ans = [[None]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        d = min(i + 1, j + 1, N - i, N - j)
        ni, nj = i, j
        for _ in range(d % 4):
            ni, nj = nj, N - 1 - ni
        ans[ni][nj] = board[i][j]

for row in ans:
    print(''.join(row))

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


"""
愚直だとオーダー(N^3)でだめ、各座標ごとの外堀を出してその外堀ごとの回転回数をmod4で計算する方針
def out_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j],end="")
        print()



def make_rotate(board, s, g):
    temp = [board[i][s:g+1] for i in range(s, g+1)]
   # print("temp")
    #out_board(temp)
    transposed = list(zip(*temp))
    rotated = [list(reversed(row)) for row in transposed]
    #print("rotated")
    #out_board(rotated)
    
    for i in range(s, g+1):
        for j in range(s, g+1):
            board[i][j] = rotated[i-s][j-s]
    #print("newboard")
   # out_board(board)
    return board

for i in range(1, N//2+1):
    board = make_rotate(board, i-1, N-i)
out_board(board)"""


N=INT()
board = []
for i in range(N):
    b = list(input())
    board.append(b)
ans = [[None]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        d = min(i + 1, j + 1, N - i, N - j)
        ni, nj = i, j
        for _ in range(d % 4):
            ni, nj = nj, N - 1 - ni
        ans[ni][nj] = board[i][j]

for row in ans:
    print(''.join(row))

>>>>>>> 5a60e3f (Sync local Atcoder directory)
