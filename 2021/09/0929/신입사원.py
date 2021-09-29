import sys
sys.stdin = open('./text/1946.txt', 'r')
input = sys.stdin.readline
for _ in range(int(input())):
    count = 1
    N = int(input())
    people = [list(map(int, input().split())) for _ in range(N)]
    people.sort() 
    Max = people[0][1]
    for i in range(1,N):
        if Max > people[i][1]:
            count += 1
            Max = people[i][1]
    print(count)