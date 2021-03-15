import sys
sys.stdin = open("14719.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
heights = list(map(int, input().split()))
S = []
result = 0
for i in range(len(heights)):
    while S and heights[i] > heights[S[-1]]:
        top = S.pop()
        if not S:
            break
        dist = i - S[-1] - 1
        waters = min(heights[i], heights[S[-1]]) - heights[top]
        result += dist * waters
    S.append(i)
print(result)
