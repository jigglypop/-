import sys
sys.stdin = open('./text/17408.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
tree = [0] * N + [Int() for _ in range(N)]
# for i in reversed(range(1, N)):



