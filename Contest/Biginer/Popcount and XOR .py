<<<<<<< HEAD
#D
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

a,b,c=MAP()
k = bin(c).count('1')

if k>a+b or (a+b-k)&1:
  print(-1)
  exit()
  
p=(a+b-k)//2

x=0
y=0

aa=a-p
bb=b-p

if aa<0 or bb<0:
  print(-1)
  exit()
  
cnt1=0  
cnt2=0

for i in range(60):
  if c&1<<i:
    if cnt1<aa:
      x+=1<<i
    else:
      y+=1<<i
    cnt1+=1
  else:
    if cnt2<p:
      cnt2+=1
      x+=1<<i
      y+=1<<i
      
if cnt1<aa+bb or cnt2<p:
  print(-1)
  exit()
x_bin=bin(x).count('1')
y_bin=bin(y).count('1')
assert x_bin==a
assert y_bin==b
assert x^y==c      
=======
#D
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

a,b,c=MAP()
k = bin(c).count('1')

if k>a+b or (a+b-k)&1:
  print(-1)
  exit()
  
p=(a+b-k)//2

x=0
y=0

aa=a-p
bb=b-p

if aa<0 or bb<0:
  print(-1)
  exit()
  
cnt1=0  
cnt2=0

for i in range(60):
  if c&1<<i:
    if cnt1<aa:
      x+=1<<i
    else:
      y+=1<<i
    cnt1+=1
  else:
    if cnt2<p:
      cnt2+=1
      x+=1<<i
      y+=1<<i
      
if cnt1<aa+bb or cnt2<p:
  print(-1)
  exit()
x_bin=bin(x).count('1')
y_bin=bin(y).count('1')
assert x_bin==a
assert y_bin==b
assert x^y==c      
>>>>>>> 5a60e3f (Sync local Atcoder directory)
print(x,y)