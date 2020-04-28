arr = [64, 25, 10, 22, 11]

# for i in range(len(arr) - 1):
#     minIdx = i
#     for j in range(i + 1, len(arr)):
#         if arr[minIdx] > arr[j]:
#             minIdx = j
#     arr[i], arr[minIdx] = arr[minIdx], arr[i]
# print(arr)

for i in range(len(arr)-1):
    m = i # 이렇게 하면 첫번째 값은 그냥들어감.
    for j in range(i + 1, len(arr)): # j를 돌릴 떄
        if arr[j] < arr[m]: # 현재 m보다 작으면
            m = j   # 교체
    arr[i], arr[m] = arr[m], arr[i] # 바꿔줌 
print(arr)