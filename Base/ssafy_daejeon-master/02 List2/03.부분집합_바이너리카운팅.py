arr = [3, 6, 7, 1, 5, 4]

for i in range(1 << len(arr)):  # i: 집합의 비트 표현 (부분집합의 원소에 대응된다 1개씩)
    for j in range(len(arr)):   # 어떤 수인지 보이게 저장시키는 것
        if i & (1 << j):        # 그 수 중에 해당 자리가 1인것을 찾아서 넣는다.
            print(arr[j], end=", ")        
    print()

# n = 10
# if n & 1:
#     print("홀수")
# else:
#     print("짝수")

