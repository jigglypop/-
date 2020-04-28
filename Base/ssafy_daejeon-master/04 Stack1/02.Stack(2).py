

class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.top = -1     # 자료가 없다는 것을 나타내기 위하여

    def push(self, item):
        self.top += 1
        self.arr[self.top] = item

    def pop(self):
        ret = self.arr[self.top]
        self.top -= 1
        return ret

    def isEmtpy(self):
        return self.top == -1

S = Stack(10)

for i in range(5):
    S.push(i)


while not S.isEmtpy():
    print(S.pop(), end=" ")
print()


# S = [0] * 3
# top = -1

# def push(item):
#     global top
#     # full-상태에 주의 if top == 마지막 인덱스
#     top += 1
#     S[top] = item

# def pop():
#     # empty-상태를 체크
#     if top == -1:return 
#     ret = S[top]
#     top -= 1
#     return ret

# S = []
# S.append(1) # push
# S.append(2)
# S.append(3)

# print(S.pop())
# print(S.pop())
# print(S.pop())
