"""
入力はグリッドのためグラフを使わずに

問題概要
高さH、幅Wの区画で通路 . を通ってスタート s からゴール g までたどり着けるか判定せよ。
ただし#は塀のため通過できない。
"""


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


from collections import deque
class Node:
    def __init__(self,index,val):
        self.index = index
        self.nears = []
        self.arrival = False
        self.val = val
        
    def __repr__(self):
        return f"(index):{self.index}, neras:{self.nears}, arrival:{self.arrival}, val:{self.val}"


#board入力しつつstart,goalの取得と移動可能マスのインスタンス作成
H,W = MAP()

#node(i,j)ご存在しているか判断するために辞書型にnodeを格納
nodes = defaultdict(lambda:Node((-1,-1),""))
for i in range(H):
    row = list(input().strip())
    for j, char in enumerate(row):
        if char =="s":
            s = (i,j)
            nodes[(i,j)] = Node((i,j),"s")
        elif char == "g":
            g = (i,j)
            nodes[(i,j)] = Node((i,j),"g")
        elif char == ".":
            nodes[(i,j)] = Node((i,j),".")
            
    
#BDS開始(startのNodeキューに入れる)
queue = deque([])
s_node = nodes[s]
s_node.arrival=True
queue.append(s_node)


#あるNODEに対してnearsを検索する関数
def search_nears(node):
    y,x = node.index
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    for j,i in zip(dx,dy):
        if 0 <= x+j < W and 0<= y+i < H: 
            if (y+i,x+j) in nodes:  #nodesにnodeがある、つまり移動可能なとき
                near_node = nodes[((y+i,x+j))]
                if near_node.val=="g":
                    print("Yes")
                    exit()
                node.nears.append((y+i,x+j))
                if  near_node.arrival== False: #未探索の物だけキューに入れる
                    near_node.arrival = True
                    queue.append(nodes[((y+i,x+j))])

while queue:
    node = queue.pop()  #pop()は深さ優先
    search_nears(node)
print("No") 


