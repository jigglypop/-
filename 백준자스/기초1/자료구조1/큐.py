import sys
from pprint import pprint
sys.stdin = open('10845.txt', 'r')


class Queue:
    def __init__(self):
        self.content = [0 for i in range(10001)]
        self.first = 0
        self.last = -1
        self.size = 0

    def push(self, item):
        self.last += 1
        self.size += 1
        self.content[self.last % 10001] = item

    def pop(self):
        if self.size == 0:
            return -1
        self.first += 1
        self.size -= 1
        return self.content[(self.first - 1) % 10001]

    def getsize(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size == 0:
            return -1
        return self.content[self.first % 10001]

    def back(self):
        if self.size == 0:
            return -1
        return self.content[self.last % 10001]


input = sys.stdin.readline
T = int(input())
queue = Queue()
for i in range(T):
    m = list(input().split())
    if m[0] == 'push':
        queue.push(m[1])
    elif m[0] == 'pop':
        print(queue.pop())
    elif m[0] == 'size':
        print(queue.getsize())
    elif m[0] == 'empty':
        print(queue.empty())
    elif m[0] == 'front':
        print(queue.front())
    elif m[0] == 'back':
        print(queue.back())
