import sys
sys.stdin = open('[백준1924번]2007년.txt', 'r')


x, y = map(int, input().split())
Day = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(x-1):
    Day = Day + arrList[i]
Day = (Day + y) % 7

print(weekList[Day])
