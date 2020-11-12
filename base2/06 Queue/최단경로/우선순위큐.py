from queue import PriorityQueue

arr = [(3,2),(2,5),(8,9),(1,4),(2,6)]

PQ = PriorityQueue()
for val in arr:
    PQ.put(val)

while not PQ.empty():
    print(PQ.get())