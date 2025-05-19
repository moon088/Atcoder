<<<<<<< HEAD
# D
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
from cmath import phase
from itertools import accumulate, chain, combinations, combinations_with_replacement, permutations, compress, dropwhile, takewhile, groupby, product, starmap
from functools import cmp_to_key,lru_cache
from operator import itemgetter, mul, xor
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush , heappop
from functools import reduce, lru_cache
from sortedcontainers import SortedSet, SortedList, SortedDict
from decimal import Decimal, ROUND_HALF_UP
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
def ROUND_OFF(X,k): return  (X // (10 ** k) + 5) // 10 * 10 ** (k + 1)
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


N,M=MAP()

def get_ab(M):
    l = []
    
    for a in range(int(sqrt(M))+1):
        b2 = M- a**2
        ng = -1; ok = M+1
        while abs(ok-ng)>1:
            mid = (ok+ng)//2
            if mid**2>=b2:
                ok=mid
            else:
                ng=mid
        if a**2+ok**2==M:
            l.append((a,ok))

    ans = set()
    for a,b in l:
        ans.update([(a,b),(b,a), (a,-b),(b,-a), (-a,-b),(-b,-a),(-a,b),(-b,a)])
    return ans


now = (0,0)
q = deque([now])
l = get_ab(M)

visited = [[INF]*N for _ in range(N)]
visited[0][0]=0
while q:
    now = q.popleft()
    for dy,dx in l:
        neary, nearx = now[0]+dy,now[1]+dx
        if isInBoard(N,N,neary,nearx) and visited[neary][nearx]>visited[now[0]][now[1]]+1:
            visited[neary][nearx]= visited[now[0]][now[1]]+1
            q.append((neary, nearx))
for i in range(N):
    for j in range(N):
        print(visited[i][j],end=" ") if visited[i][j]<INF else print(-1,end=" ")
    print()


=======
# D
import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, atan2, radians, degrees, log2, gcd
from cmath import phase
from itertools import accumulate, chain, combinations, combinations_with_replacement, permutations, compress, dropwhile, takewhile, groupby, product, starmap
from functools import cmp_to_key,lru_cache
from operator import itemgetter, mul, xor
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush , heappop
from functools import reduce, lru_cache
from sortedcontainers import SortedSet, SortedList, SortedDict
from decimal import Decimal, ROUND_HALF_UP
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
def ROUND_OFF(X,k): return  (X // (10 ** k) + 5) // 10 * 10 ** (k + 1)
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


N,M=MAP()

def get_ab(M):
    l = []
    
    for a in range(int(sqrt(M))+1):
        b2 = M- a**2
        ng = -1; ok = M+1
        while abs(ok-ng)>1:
            mid = (ok+ng)//2
            if mid**2>=b2:
                ok=mid
            else:
                ng=mid
        if a**2+ok**2==M:
            l.append((a,ok))

    ans = set()
    for a,b in l:
        ans.update([(a,b),(b,a), (a,-b),(b,-a), (-a,-b),(-b,-a),(-a,b),(-b,a)])
    return ans


now = (0,0)
q = deque([now])
l = get_ab(M)

visited = [[INF]*N for _ in range(N)]
visited[0][0]=0
while q:
    now = q.popleft()
    for dy,dx in l:
        neary, nearx = now[0]+dy,now[1]+dx
        if isInBoard(N,N,neary,nearx) and visited[neary][nearx]>visited[now[0]][now[1]]+1:
            visited[neary][nearx]= visited[now[0]][now[1]]+1
            q.append((neary, nearx))
for i in range(N):
    for j in range(N):
        print(visited[i][j],end=" ") if visited[i][j]<INF else print(-1,end=" ")
    print()


>>>>>>> 5a60e3f (Sync local Atcoder directory)
            