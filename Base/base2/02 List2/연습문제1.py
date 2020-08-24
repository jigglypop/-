import pprint

arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]


dy = [-1,1,0,0]
dx = [0,0,1,-1]

r = [[0]*7 for _ in range(7)]
s = [[0]*7 for _ in range(7)]
for y in range(1,6):
    for x in range(1,6):
        s[y][x] = 1

arr2 = [[0]*7]
for y in arr:
    arr2.append([0]+y+[0])
arr2.append([0]*7)

pprint.pprint(arr2)
pprint.pprint(s) 

ny = 0
nx = 0
for y in range(1,6):
    for x in range(1,6):
        for i in range(4):
            nx = x + dx
            ny = y + dy
            r[y][x] = abs(arr[y][x]-arr[ny][nx] * s[ny][nx])
pprint.pprint(r)
        
            


