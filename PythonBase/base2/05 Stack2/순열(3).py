# arr = 'ABC'
# N = len(arr)

# # 3*2*1 로 구함
# for i in range(N):
#     for j in range(N):
#         if i == j:continue
#         for k in range(N):
#             if i == k or j == k:continue
#             print(arr[i],arr[j],arr[k])

arr = 'ABC'
N = len(arr)

order = [0] * N # 실제 요소들의 순서(index를 기록)

def perm(k,n):
    if k == n:
        for i in range(N):
            print(arr[order[i]],end=' ')
        print()
        return
    used = [False] * N  # 지금까지 선택한 원소들의 집합
    for i in range(k):  # 지금까지 선택한 k개의 원소를 확인
        used[order[i]] = True

    for i in range(N):  # 선택하지 않은 요소들에 대해
        if used[i]:continue
        order[k] = i
        perm(k+1,n)

perm(0,N)