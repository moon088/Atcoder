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
def YES(): return print("Yes")
def NO(): return print("No")
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 1 << 60

N,S,T=MAP()
graph = []
for i in range(N):
    a,b,c,d=MAP()
    graph.append([(a,b), (c,d)])

base = sum(sqrt(abs(graph[i][0][0]-graph[i][1][0])**2 + abs(graph[i][0][1]-graph[i][1][1])**2) for i in range(N))/T
#print(base)

def get_other_end(current_point):
    """
    直線と端点を表すタプルを入力として受け取り、そのタプルが表す直線のもう一方の端点を返す関数。

    Args:
      current_point: 直線と端点を表すタプル。

    Returns:
      入力されたタプルが表す直線のもう一方の端点を表すタプル。
    """
    line, end = current_point
    return (line, 1 - end)  # end が 0 なら 1 を、1 なら 0 を返す

def generate_valid_routes(lines):
    """
    条件を満たす順路を生成する関数。

    Args:
      lines: 直線と端点を表すタプルのリスト。

    Returns:
      条件を満たす順路のリスト。
    """
    result = []
    if not lines:
        return [[]]

    for i, first_point in enumerate(lines):
        remaining_lines = lines[:i] + lines[i+1:]
        second_point = get_other_end(first_point)
        if second_point in remaining_lines:
            remaining_lines.remove(second_point)
            for route in generate_valid_routes(remaining_lines):
                result.append([first_point, second_point] + route)
    return result


lines = []
for i in range(N):
    for j in range(2):
        lines.append((i,j))


valid_routes = generate_valid_routes(lines)
#print(valid_routes)

ans=INF
for i in range(len(valid_routes)):
    cost = 0.0
    now = (0,0)
    for j in range(0,2*N):
        if j%2==0:
            next_x , next_y= graph[valid_routes[i][j][0]][valid_routes[i][j][1]]
            if j==0:
                now_x, now_y = (0,0)
            else:
                now_x, now_y = graph[now[0]][now[1]]
           # print(now_x,now_y,next_x,next_y)
            cost += sqrt(abs(now_x - next_x)**2 + abs(now_y - next_y)**2)
        else:
            now=valid_routes[i][j]
   # print(cost)
    ans = min(ans, cost)            
ans = ans/S + base
print(ans)