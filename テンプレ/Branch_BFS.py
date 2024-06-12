"""
キューによる実装！！入力は既にグラフである

問題概要
入力
N M
A_1 B_1
...
A_M B_M

部屋A_Kから部屋B_Kへは通行ができる。
このとき部屋1～通路を通って部屋2～部屋Nすべてに到達できるのかYes,Noを出力し、
その経路の部屋iが次に移動する部屋番号を出力する
"""

from collections import deque
class Node:
    """
    ノード情報の管理
    Attributes:
        index (int): ノード番号
        nears (list): 隣接リスト（隣接するノード番号を格納）
        parentがこれでもあり-> arrival (bool): 探索済フラグ（到達済の場合Trueが返される）
        parent (int):親のノード番号
    """
    
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.parent = -1

    def __repr__(self):
        return f"(index:{self.index}, nears:{self.nears}, parent:{self.parent})"



N,M=map(int,input().split())

#Nodeインスタンスをnodeに格納
nodes = [Node(i) for i in range(N+1)]

for _ in range(M):
    start, goal = map(int,input().split())
    nodes[start].nears.append(goal)
    nodes[goal].nears.append(start)
    
#探索するqueue作成
#deque(a)で[a]を作成
#pop(),popleft()が取り出し 
#append(),appendleft()が挿入
#extend(),extendleft()で[p,q]などすべて追加
queue = deque([])

queue.append(nodes[1])
nodes[1].parent=0

##BFS開始
while queue:
    node = queue.popleft() #popleft()で幅優先
    nears = node.nears
    
    #すべてのnodeの隣接ノードに対して親設定とみ探索ノードのキューに追加を行う
    for near in nears:
        if nodes[near].parent == -1:
            queue.append(nodes[near])
            nodes[near].parent = node.index

ans = [nodes[i].parent for i in range(2,N+1)]
#親ノードの情報ansに-1が含まれていればみ探索のためたどりつけないノードが存在する

if -1 in ans:
    print("No")
else:
    print("Yes")
    for i in ans:
        print(i)


