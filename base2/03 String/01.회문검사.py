# def isPalindrome(arr):
#     N = len(arr)
#     cnt = N // 2 
#     # 반만 조사한다.

#     i = 0
#     while i < cnt:
#         if arr[i] != arr[N - 1 - i]:
#             return False
#         i += 1
#     return True


# arr1 = 'abacxcaba'
# arr2 = 'bbbbabbb'

# print(isPalindrome(arr1))
# print(isPalindrome(arr2))


#--------------------------------------

# def isPalindrome(arr):


# arr1 = 'abacxcaba'
# arr2 = 'bbbbabbb'

# print(isPalindrome(arr1))
# print(isPalindrome(arr2))


#---------------------------------------
def isPalindrome(arr):
    # 반만 조사한다.
    i = 0
    while i < len(arr) // 2:
        if arr[i] != arr[len(arr) - 1 - i]:
            return False
        i += 1
    return True


arr1 = 'abacxcaba'
arr2 = 'bbbbabbb'

print(isPalindrome(arr1))
print(isPalindrome(arr2))