from LinkedList import List, Node

#-------------------------------------------------
import time
start = time.time()
# ------------------------------------------------

mylist = List()
mylist.insertfirst(Node(1))
mylist.insertfirst(Node(2))
mylist.insertfirst(Node(3))
mylist.printlist()

mylist.insertfirst(Node(4))
mylist.insertfirst(Node(5))
mylist.printlist()

#-------------------------------------------------
print("time :", time.time() - start)