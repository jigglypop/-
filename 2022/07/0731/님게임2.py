import sys
sys.stdin = open('./text/11868.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip().split()
x = 0
for y in Str():
    x ^= int(y)
print("koosaga" if x else "cubelover")