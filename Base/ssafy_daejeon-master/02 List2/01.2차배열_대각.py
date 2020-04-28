arr = [[ 1,  2,  4,  7, 11],
       [ 3,  5,  8, 12, 15],
       [ 6,  9, 13, 16, 18],
       [10, 14, 17, 19, 20]]

# 사선의 수 8개 : 4행 5열일 때 4+5-1 


N, M = len(arr), len(arr[0])
for diag in range(0, N + M - 1):    # diag: 사선의 수 # x, y: 시작 좌표    
    x = 0 if diag < M else (diag - M + 1)
    # 1. M까지 쭉 순회하고 N방향으로 갈 때 diag - M + 1
    y = diag if diag < M else M - 1
    # 2. N방향일 때 
    while x < N and y >= 0:
    # x는 늘어나므로 최고값 제한, y는 줄어들어서 >=0
        print('%2d ' % arr[x][y], end='')
        x += 1
        y -= 1
    print()

# 1. 행 우선순회
# for y in range(len(arr)):
#     for x in range(len(arr[0])):
#         arr[y][x]

# 2. 열 우선순회
# for x in range(len(arr[0])):
#     for y in range(len(arr)):
#         arr[y][x]
