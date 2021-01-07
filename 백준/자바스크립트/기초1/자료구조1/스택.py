import sys
from pprint import pprint
sys.stdin = open('10828.txt', 'r')


class Stack:
    def __init__(self):
        self.S = []
        self.length = 0

    def push(self, x):
        return self.S.append(x)

    def top(self):
        if len(self.S) == 0:
            return -1
        return self.S[-1]

    def size(self):
        return len(self.S)

    def empty(self):
        if len(self.S) == 0:
            return 1
        return 0

    def pop(self):
        if len(self.S) == 0:
            return -1
        return self.S.pop()


input = sys.stdin.readline
T = int(input())
stack = Stack()
for i in range(T):
    m = list(input().split())
    if m[0] == 'push':
        stack.push(m[1])
    elif m[0] == 'top':
        print(stack.top())
    elif m[0] == 'size':
        print(stack.size())
    elif m[0] == 'empty':
        print(stack.empty())
    elif m[0] == 'pop':
        print(stack.pop())
