"""
問題
https://atcoder.jp/contests/arc005/tasks/arc005_3
s->gまで行くとき#を2回まで超えることができる。このときgまでたどり着けるかどうか    
"""

from collections import deque, defaultdict, Counter
from heapq import heappush , heappop
def MAP(): return map(int, input().split())
def LIST(): return list(map(int,  input().split()))
def BOARD(H): return [list(input().strip()) for _ in range(H)]
Dxy = [(1,0),(-1,0),(0,1),(0,-1)]


H,W = MAP()
board = BOARD(H)

for i in range(H):
    for j in range(W):
        if board[i][j] == "s":
            sx = j
            sy = i
        elif board[i][j] == "g":
            gx = j
            gy = i

#距離は#なら1、ほか0の重みとしてとらえる
queue = deque([(sx,sy)])
inf = 10**9
dis = [[inf]*W for _ in range(H)]
dis[sy][sx]=0

while queue:
    x,y = queue.popleft()
    for dx, dy in Dxy:
        if 0<=x+dx<W and 0<=y+dy<H :
            #print(y+dy,x+dx)
            if dis[y+dy][x+dx] == inf:#未探索
                if board[y+dy][x+dx]=="#":
                    dis[y+dy][x+dx] = dis[y][x]+1
                    queue.append((x+dx,y+dy)) #右端にいれる
                else:
                    dis[y+dy][x+dx]=dis[y][x]
                    queue.appendleft((x+dx,y+dy)) #左端に入れる

if dis[gy][gx]<=2:
    print("YES")
else:
    print("NO")