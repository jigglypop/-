import sys
sys.stdin = open("2693.txt", "r")
input = sys.stdin.readline
for _ in range(int(input())):
    temp = list(map(int, input().split()))
    temp.sort(reverse=True)
    print(temp[2])
