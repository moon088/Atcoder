# F
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


class LinearSieve:
    def __init__(self,maxN):self.sievedList=self.Sieve(maxN);self.maxN=maxN
    def Sieve(self,R):  #1≦N≦R の最小素因数表を作成する
        if not isinstance(R,int):return -1
        if R<=1:return -1
        Large=[None for i in range(R+1)];Large[:2]=[0,1];Prime=[]
        for i in range(2,R+1):
            if Large[i]==None:Large[i]=i;Prime.append(i)
            for p in Prime:
                if p*i>R or p>Large[i]:break
                Large[p*i]=p
        return Large     
    def Fact(self,x):  #xを高速素因数分解する
        if not isinstance(x,int):return -1
        if len(self.sievedList)<=x:return -1
        if x==1:return[[1,1]]
        Ans=[]
        while 1:
            if self.sievedList[x]==x:Ans.append(x);break
            Ans.append(self.sievedList[x]);x//=self.sievedList[x]
        Key=set(Ans);D={i:0 for i in Key}
        for i in Ans:D[i]+=1
        return [(i,D[i]) for i in D]
    def ALLdiv(self,x):  #約数列挙する
        L=self.Fact(x);Div=set([1])
        for i,j in L:
            NewDiv=set()
            for d in Div:
                for k in range(1,j+1):NewDiv.add(d*i**k)
            Div=Div.union(NewDiv)
        return Div 
    def PrimeList(self,x,y):  #x≦P≦y の素数を列挙する
        x,y=max(0,x),min(y,self.maxN)
        return [i for i in range(x,y+1) if self.sievedList[i]==i and i>1]




N=INT()
A=LIST()
LS = LinearSieve(10 ** 5)
D = [-1] * (max(A) + 1)
D[1] = 0
for x in range(2, max(A) + 1):
    S = set()
    T = LS.ALLdiv(x) #約数列挙
    for i in T:
        S.add(D[i]) #約数のGrundy数を集合にためてmex求める
    for i in range(10 ** 6):
        if i not in S:
            D[x] = i#　MEX発見したのでそれがGrandy数
            break

ans = 0
for Ai in A:
    ans ^= D[Ai]
#print(ans)
print('Anna' if ans else 'Bruno')

