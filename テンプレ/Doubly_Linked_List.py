# ノードクラス(辞書により挿入(削除)ノードの探索はオーダー1になっている)

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
            print(current.data, end=" <-> ")
            current = current.next
        print("None")