import pprint

arr = [[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]


for y in range(len(arr)):
    for x in range(len(arr)):
        if x < y:
            arr[x][y], arr[y][x] = arr[y][x], arr[x][y]


pprint.pprint(arr)