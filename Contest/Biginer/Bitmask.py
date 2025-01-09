# D
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
def isInBoard(H,W,y,x): return 0<=y<=H and 0<=x<W
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60


S=input()
N=INT()

N_bin = [] 
while N>0:
    N_bin.append(N%2)
    N//=2
N_bin.reverse()


flag = False
if len(N_bin)<len(S):
    N_bin = [0]*abs(len(N_bin)-len(S)) + N_bin
elif len(N_bin)>len(S):
    S = "0"*abs(len(N_bin)-len(S)) + S
print(S,N_bin)
ans = []
temp=[]
for i in range(len(S)):
    if flag:
        if S[i]=="?":
            ans.append(1)
        else:
            ans.append(int(S[i]))
    else:
        if S[i]=="0":
            if N_bin[i]==1:
                flag=True
                if temp:
                    idx = temp.pop()
                    ans.insert(idx,1)
            ans.append(0)
        elif S[i]=="1":
            if N_bin[i]==0:
                if not temp:
                    print(-1)
                    exit()
                else:
                    idx = temp.pop()
                    ans.insert(idx,0)
                    flag=True
                    ans.append(1)
            else:
                ans.append(1)
        else:
            if N_bin[i]==0:
                ans.append(0)
            else:
                if temp:
                    idx = temp.pop()
                    ans.insert(idx, 1)
                temp.append(i)
if not flag:
    if temp:
        idx = temp.pop()
        ans.insert(idx, 1)
fin = 0
print(ans)

for bit in ans:
    fin = fin*2+bit
print(fin)