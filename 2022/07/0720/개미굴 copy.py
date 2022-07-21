import sys
sys.stdin = open('./text/14275.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

head = {}

def add(head, words):
    for word in words:
        if word not in head:
            head[word] = {}
        head = head[word]
    head['*'] = True
    return head

def search(head, words):
    for word in words:
        if word not in head:
            return False
        head = head[word]
    return True if head['*'] else False

N = int(input())
word_set = [list(input().split())[1:] for _ in range(N)]

for words in word_set:
    print(words)
    head = add(head, words)
print(head)
def solve(heads, k):
    if '*' in heads:
        return
    keys = list(heads.keys())
    keys.sort()
    for key in keys:
        value = heads[key]
        print('--' * k + str(key))
        solve(value, k + 1)

solve(head, 0)