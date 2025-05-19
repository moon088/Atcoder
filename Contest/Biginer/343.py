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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N=INT()

def is_cube(num):
    cube_root = round(num**(1/3))
    return cube_root ** 3==num,cube_root

def search_root(num):
    for i in range(num,-1,-1):
        result=is_cube(i)
        if result[0]:
            return result[1]
    return False

k=1
while k**3 <=N:
    num=k**3
    digit = [int(d) for d in str(num)]
    flag=True
    for j in range(len(digit)//2):
        if digit[j]==digit[len(digit)-j-1]:
            continue
        else:
            flag=False
            break
    if flag:
        temp=num
    k+=1
print(temp)

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
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N=INT()

def is_cube(num):
    cube_root = round(num**(1/3))
    return cube_root ** 3==num,cube_root

def search_root(num):
    for i in range(num,-1,-1):
        result=is_cube(i)
        if result[0]:
            return result[1]
    return False

k=1
while k**3 <=N:
    num=k**3
    digit = [int(d) for d in str(num)]
    flag=True
    for j in range(len(digit)//2):
        if digit[j]==digit[len(digit)-j-1]:
            continue
        else:
            flag=False
            break
    if flag:
        temp=num
    k+=1
print(temp)

>>>>>>> 5a60e3f (Sync local Atcoder directory)
