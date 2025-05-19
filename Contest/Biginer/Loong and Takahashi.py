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

N = INT()
board = [[0]*N for _ in range(N)]
cnt = 1
temp = [0,0]
Dxy = [(0,1), (1,0), (0,-1), (-1,0)]
Dxy_num = 0
board[N//2][N//2]="T"
while cnt <= N**2 -1:
    board[temp[0]][temp[1]] = cnt
    cnt += 1

    #print(temp)
    if  not 0<=temp[0]+ Dxy[Dxy_num][0]<=N-1 or not 0<= temp[1]+Dxy[Dxy_num][1]<=N-1 or board[temp[0]+Dxy[Dxy_num][0]][temp[1]+Dxy[Dxy_num][1]]:
        Dxy_num = (Dxy_num+1)%4
    
    temp[0] +=  Dxy[Dxy_num][0]
    temp[1] +=  Dxy[Dxy_num][1]

for i in range(N):
    print(*board[i])
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

N = INT()
board = [[0]*N for _ in range(N)]
cnt = 1
temp = [0,0]
Dxy = [(0,1), (1,0), (0,-1), (-1,0)]
Dxy_num = 0
board[N//2][N//2]="T"
while cnt <= N**2 -1:
    board[temp[0]][temp[1]] = cnt
    cnt += 1

    #print(temp)
    if  not 0<=temp[0]+ Dxy[Dxy_num][0]<=N-1 or not 0<= temp[1]+Dxy[Dxy_num][1]<=N-1 or board[temp[0]+Dxy[Dxy_num][0]][temp[1]+Dxy[Dxy_num][1]]:
        Dxy_num = (Dxy_num+1)%4
    
    temp[0] +=  Dxy[Dxy_num][0]
    temp[1] +=  Dxy[Dxy_num][1]

for i in range(N):
    print(*board[i])
>>>>>>> 5a60e3f (Sync local Atcoder directory)
