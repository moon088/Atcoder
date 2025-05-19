<<<<<<< HEAD
# B
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

H,W=MAP()
Si,Sj = MAP()
Si-=1
Sj-=1
board = BOARD(H)
X=input()

for i in range(len(X)):
    if X[i]=="R":
        direction = Dxy[2]
    elif X[i]=="L":
        direction = Dxy[3]
    elif X[i]=="U":
        direction = Dxy[1]
    else:
        direction = Dxy[0]
    if 0<=Si+direction[0]<H and 0<=Sj+direction[1]<W and board[Si+direction[0]][Sj+direction[1]]==".":
        Si+=direction[0]
        Sj+=direction[1]
    #print(Si,Sj)
=======
# B
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

H,W=MAP()
Si,Sj = MAP()
Si-=1
Sj-=1
board = BOARD(H)
X=input()

for i in range(len(X)):
    if X[i]=="R":
        direction = Dxy[2]
    elif X[i]=="L":
        direction = Dxy[3]
    elif X[i]=="U":
        direction = Dxy[1]
    else:
        direction = Dxy[0]
    if 0<=Si+direction[0]<H and 0<=Sj+direction[1]<W and board[Si+direction[0]][Sj+direction[1]]==".":
        Si+=direction[0]
        Sj+=direction[1]
    #print(Si,Sj)
>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(Si+1, Sj+1)