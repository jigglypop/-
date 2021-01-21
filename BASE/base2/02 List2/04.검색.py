# 순서대로 검색하는 방법. 가장 기본적
def sequence_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key: return i
    return '없음'


# 이진검색
# 반드시 정렬된 상태여야 한다.

def binarySearch(arr,lo,hi,key):
    if lo > hi:
        return False    
    mid = (lo+hi) >> 1 # //써도 됨
    if arr[mid] == key:
        return True
    elif arr[mid] > key:
        # mid는 볼 필요 없음
        return binarySearch(arr,lo,mid - 1,key)
    else:
        return binarySearch(arr,mid + 1,hi,key)
    

def binary_Search(arr,lo,hi,key):
    lo,hi = 0, len(arr) -1
    # lo = 범위의 시작인덱스, hi = 범위의 끝 인덱스
    # 계속 줄다가 같아질 때까지 해야함
    # 못찾으면 lo가 hi보다 커지게 됨
    while lo <= hi:
        mid = (lo+hi) >> 1 # //써도 됨
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            hi = mid - 1 # mid는 볼 필요 없음
        else:
            lo = mid + 1 
    return False


arr = [2, 5, 7, 8, 12, 16, 21, 23, 33, 39, 42, 45, 45, 49, 62, 88]

hi = len(arr) - 1
print(sequence_search(arr, 39))
print(sequence_search(arr, 50))

print(binary_Search(arr, 0, hi, 39))
print(binary_Search(arr, 0, hi, 50))

print(binarySearch(arr, 0, hi, 39))
print(binarySearch(arr, 0, hi, 50))

print("---------------------------------------")

# ------------------------------------------------------
# bisect 라이브러리 사용
from bisect import bisect, bisect_left, bisect_right


print(bisect_left(arr, 39))     # bisect()와 혼동하지 말것, 범위 지정 가능
print(bisect_left(arr, 50))     # 결과값 무엇?
print(bisect_right(arr, 45))


