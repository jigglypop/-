import pprint



N,M = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(N)]

chicken= []
house = []
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1:
            house.append((y,x))
        elif arr[y][x] == 2:
            chicken.append((y,x))
pprint.pprint(len(chicken))
pprint.pprint(len(house))