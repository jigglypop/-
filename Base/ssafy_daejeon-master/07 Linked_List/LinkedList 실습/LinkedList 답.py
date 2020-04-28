class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __del__ (self):
        print(self.data, '삭제')
class List:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
#---------------------printlist--------------------
    def printlist(self):
        if self.head is None: # 공백 리스트인지 체크
            return
        cur = self.head
        while cur is not None:
            print(cur.data, end = ' ')
            cur = cur.next
        print()
#---------------------insertlast--------------------
    def insertlast(self,node):
        if self.head is None:           # 빈리스트
            self.head = self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
#---------------------insertfirst--------------------
    def insertfirst(self,node):
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
#---------------------deletelast--------------------
    def deletelast(self):
        if self.head is None:
            return
        prev, cur = None, self.head
        while cur.next is not None:
            cur = cur.next
        if prev is None:
            self.head = self.tail = None
        else:
            prev.next = None
            self.tail = prev
        del cur
        self.size -= 1
#---------------------deletefirst--------------------
    def deletefirst(self):
        if self.head is None:
            return
        cur = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = cur.next
        del cur
        self.size -= 1        
#---------------------insertAt--------------------
    def insertAt(self,idx,node):        # idx: 삽입 위치, node: 삽입 노드
        if self.head is None:
            self.head = self.tail = node
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1
            if prev is None:
                node.next = cur
                self.head = node
            elif cur is None:
                prev.next = self.tail = node
            else:
                node.next = cur
                prev.next = node
            self.size += 1
       