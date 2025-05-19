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

N=INT()
A=LIST()
k = (N+1) // 2 
#Nが偶数ならk,k+1

def search_size(k,A):
    center =A[k]
    right = A[k-1:]
    left = A[k-1::-1]
    #print(right, left)
    i = 0
    size = k
    while i < len(right):
        temp1 = right[i]
        temp2 = left[i]
        val = min(temp1, temp2)
        #print(size, val)
        if val < size-i:
            gensyou = size-i-val
            size -= gensyou
            for _ in range(gensyou):
                right.pop()
                left.pop()
            if size < i:
                return i
            i+=1
        else:
            i+=1
            continue    
    return size

if N==1:
    print(1)
    exit()
elif N==2:
    print(1)
    exit()
elif N % 2== 1:
    ans = search_size(k,A)
else:
    ans = max(search_size(k,A[:len(A-2)]), search_size(k+1,A[1:]))

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

N=INT()
A=LIST()
k = (N+1) // 2 
#Nが偶数ならk,k+1

def search_size(k,A):
    center =A[k]
    right = A[k-1:]
    left = A[k-1::-1]
    #print(right, left)
    i = 0
    size = k
    while i < len(right):
        temp1 = right[i]
        temp2 = left[i]
        val = min(temp1, temp2)
        #print(size, val)
        if val < size-i:
            gensyou = size-i-val
            size -= gensyou
            for _ in range(gensyou):
                right.pop()
                left.pop()
            if size < i:
                return i
            i+=1
        else:
            i+=1
            continue    
    return size

if N==1:
    print(1)
    exit()
elif N==2:
    print(1)
    exit()
elif N % 2== 1:
    ans = search_size(k,A)
else:
    ans = max(search_size(k,A[:len(A-2)]), search_size(k+1,A[1:]))

>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(ans)