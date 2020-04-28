class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __del__ (self):
        print(self.data,'삭제')

class List:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0

#---------------------printlist--------------------
    def printlist(self):
        
#---------------------insertlast--------------------
    def insertlast(self,node):
        
#---------------------insertfirst--------------------
    def insertfirst(self,node):
        
#---------------------deletelast--------------------
    def deletelast(self):
       
#---------------------deletefirst--------------------
    def deletefirst(self):
              
#---------------------insertAt--------------------
    def insertAt(self,idx,node):        # idx: 삽입 위치, node: 삽입 노드
       