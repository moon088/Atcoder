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
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N,T=MAP()
S=input()
X=LIST()
flag=S[0]

mainasu=[]
purasu=[]
af_purasu =[]

for i in range(N):
    if int(S[i])==0:
        mainasu.append(X[i])    
    else:
        purasu.append(X[i])
        af_purasu.append(X[i]+2*T)
#print(mainasu,purasu)
purasu.sort()
af_purasu.sort()

def count_pairs(purasu,afpurasu,mainasu):
    n = len(purasu)
    m = len(mainasu)
    pair_count = 0
    af_pair_cnt=0
        
    for j in range(m):
        idx = bisect_left(purasu, mainasu[j])
        after_idx = bisect_left(afpurasu, mainasu[j])
       # print(2313,after_idx)
        pair_count += n - idx  
        af_pair_cnt += n- after_idx
        #print(n-idx,n-after_idx)
    return pair_count,af_pair_cnt


res = count_pairs(purasu,af_purasu,mainasu)
#print(res)
print(res[1]-res[0])



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
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def MIXED_LIST(): return [int(x) if x.isdigit() else x for x in input().split()]
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N,T=MAP()
S=input()
X=LIST()
flag=S[0]

mainasu=[]
purasu=[]
af_purasu =[]

for i in range(N):
    if int(S[i])==0:
        mainasu.append(X[i])    
    else:
        purasu.append(X[i])
        af_purasu.append(X[i]+2*T)
#print(mainasu,purasu)
purasu.sort()
af_purasu.sort()

def count_pairs(purasu,afpurasu,mainasu):
    n = len(purasu)
    m = len(mainasu)
    pair_count = 0
    af_pair_cnt=0
        
    for j in range(m):
        idx = bisect_left(purasu, mainasu[j])
        after_idx = bisect_left(afpurasu, mainasu[j])
       # print(2313,after_idx)
        pair_count += n - idx  
        af_pair_cnt += n- after_idx
        #print(n-idx,n-after_idx)
    return pair_count,af_pair_cnt


res = count_pairs(purasu,af_purasu,mainasu)
#print(res)
print(res[1]-res[0])



>>>>>>> 5a60e3f (Sync local Atcoder directory)
