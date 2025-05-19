<<<<<<< HEAD
# E
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


# ノードクラス
class Node:
    #コンストラクタ
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None
    
#双方向リストクラス
class DoublyLinkedList:
    def __init__(self):
       self.head = None
       self.tail = None
       self.length = 0
       self.node_map = {}
       
    #先頭に入れる
    def push(self, new_data): 
        new_node = Node(new_data) 
        self.node_map[new_data] = new_node
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length  += 1


    #末尾に入れる
    def append(self, new_data):  
        new_node = Node(new_data)
        self.node_map[new_data] = new_node 
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        
        
    #(index)に挿入(push,appendも実装できてる)
    def insert_at_index(self, data, position):
        if position < 0 or position > self.length:
            raise IndexError("Index out of range")

        if position ==0:
            self.push(data)
            return
        elif position == self.length:
            self.append(data)
            return
        
        new_node = Node(data)
        self.node_map[data] = new_node 
        cur = self.head 
        cur_pos = 0
        
        while cur and cur_pos < position:
            cur = cur.next
            cur_pos += 1
        
        cur.prev.next = new_node
        new_node.prev = cur.prev
        new_node.next = cur
        cur.prev = new_node
        
        self.legnth += 1


    #(node)の直後に挿入
    def insert_after_val(self, val, data):
        if val not in self.node_map:
            raise ValueError("Value not found in the list")
        new_node = Node(data)
        self.node_map[data] = new_node  # ノードを辞書に追加
        cur = self.node_map[val]
        new_node.next = cur.next
        new_node.prev = cur
        if cur.next:
            cur.next.prev = new_node
        cur.next = new_node
        if new_node.next is None:
            self.tail = new_node
        self.length += 1
        
       
    #指定nodeの削除
    def delete(self,data):
        if not self.head:
            return
        
        node = self.node_map[data]

        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif node == self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None 
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
        self.length -= 1
        
        
    #双方向リストを可視化
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

        
          
N=INT()
A=LIST()
Q=INT()

doubly = DoublyLinkedList()
for i in A:
    len = doubly.length
    doubly.insert_at_index(i, len)

for i in range(Q):
    flag, *pair = MAP()

    if flag == 1:
        doubly.insert_after_val(pair[0],pair[1])
    else:
        doubly.delete(pair[0])
=======
# E
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


# ノードクラス
class Node:
    #コンストラクタ
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None
    
#双方向リストクラス
class DoublyLinkedList:
    def __init__(self):
       self.head = None
       self.tail = None
       self.length = 0
       self.node_map = {}
       
    #先頭に入れる
    def push(self, new_data): 
        new_node = Node(new_data) 
        self.node_map[new_data] = new_node
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length  += 1


    #末尾に入れる
    def append(self, new_data):  
        new_node = Node(new_data)
        self.node_map[new_data] = new_node 
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        
        
    #(index)に挿入(push,appendも実装できてる)
    def insert_at_index(self, data, position):
        if position < 0 or position > self.length:
            raise IndexError("Index out of range")

        if position ==0:
            self.push(data)
            return
        elif position == self.length:
            self.append(data)
            return
        
        new_node = Node(data)
        self.node_map[data] = new_node 
        cur = self.head 
        cur_pos = 0
        
        while cur and cur_pos < position:
            cur = cur.next
            cur_pos += 1
        
        cur.prev.next = new_node
        new_node.prev = cur.prev
        new_node.next = cur
        cur.prev = new_node
        
        self.legnth += 1


    #(node)の直後に挿入
    def insert_after_val(self, val, data):
        if val not in self.node_map:
            raise ValueError("Value not found in the list")
        new_node = Node(data)
        self.node_map[data] = new_node  # ノードを辞書に追加
        cur = self.node_map[val]
        new_node.next = cur.next
        new_node.prev = cur
        if cur.next:
            cur.next.prev = new_node
        cur.next = new_node
        if new_node.next is None:
            self.tail = new_node
        self.length += 1
        
       
    #指定nodeの削除
    def delete(self,data):
        if not self.head:
            return
        
        node = self.node_map[data]

        if node == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif node == self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None 
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
        self.length -= 1
        
        
    #双方向リストを可視化
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

        
          
N=INT()
A=LIST()
Q=INT()

doubly = DoublyLinkedList()
for i in A:
    len = doubly.length
    doubly.insert_at_index(i, len)

for i in range(Q):
    flag, *pair = MAP()

    if flag == 1:
        doubly.insert_after_val(pair[0],pair[1])
    else:
        doubly.delete(pair[0])
>>>>>>> 5a60e3f (Sync local Atcoder directory)
doubly.display()