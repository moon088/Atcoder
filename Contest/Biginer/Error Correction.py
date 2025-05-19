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

N, T = input().split()
N = int(N)

def isJushi(s):
    if len(s)==len(T):
        flag=False
        for i in range(len(s)):
            if s[i]==T[i]:
                continue
            if s[i]!=T[i] and not flag:
                flag=True
            else:
                return False
        return True                
        
    elif len(s)==len(T)+1:
        i=0
        j=0
        while i<len(s):
            if j==len(T):
                return True
            if s[i] == T[j]:
                i+=1
                j+=1
                continue
            elif s[i]!=T[j] and i==j:
                i+=1
            else:
                return False
        return True
    
    elif len(s)+1==len(T):
        i=0
        j=0
        while j<len(T):
            if i==len(s):
                return True                
            if s[i]==T[j]:
                i+=1
                j+=1
                continue
            elif s[i]!=T[j] and i==j:
                j+=1
            else:
                return False
        return True

ans=[]
for i in range(N):
    s = input()  
    if isJushi(s):
        ans.append(i)

print(len(ans))
for i in ans:
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

N, T = input().split()
N = int(N)

def isJushi(s):
    if len(s)==len(T):
        flag=False
        for i in range(len(s)):
            if s[i]==T[i]:
                continue
            if s[i]!=T[i] and not flag:
                flag=True
            else:
                return False
        return True                
        
    elif len(s)==len(T)+1:
        i=0
        j=0
        while i<len(s):
            if j==len(T):
                return True
            if s[i] == T[j]:
                i+=1
                j+=1
                continue
            elif s[i]!=T[j] and i==j:
                i+=1
            else:
                return False
        return True
    
    elif len(s)+1==len(T):
        i=0
        j=0
        while j<len(T):
            if i==len(s):
                return True                
            if s[i]==T[j]:
                i+=1
                j+=1
                continue
            elif s[i]!=T[j] and i==j:
                j+=1
            else:
                return False
        return True

ans=[]
for i in range(N):
    s = input()  
    if isJushi(s):
        ans.append(i)

print(len(ans))
for i in ans:
>>>>>>> 5a60e3f (Sync local Atcoder directory)
    print(i+1, end=" ")