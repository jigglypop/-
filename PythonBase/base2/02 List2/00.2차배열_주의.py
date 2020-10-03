arr1 = [[1,2], [3,4]]
arr2 = [arr1[0]]
arr1[0][0] = 100
print(arr1)
print(arr2)


# # 방법 1 - 나의 실수
# list1 = [[0] * 3] * 3
# list1[0][0] = 1
# print(list1)        # [[1,0,0],[1,0,0],[1,0,0]]

# 방법 2
list2 = [[0] * 3 for _ in range(3)]
list2[0][0] = 1
print(list2)        # [[1,0,0],[0,0,0],[0,0,0]]



