import string
import sys
from pprint import pprint


def caesar(s, n):
    result = ""
    base = ""
    for i in s:
        if i in string.ascii_lowercase:
            base = string.ascii_lowercase
        elif i in string.ascii_uppercase:
            base = string.ascii_uppercase
        else:
            result += i
            continue
        a = base.index(i) + n
        result += base[a % len(base)]
    return result


def LCS(A, B):
    arr = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
    for i in range(len(B)):
        for j in range(len(A)):
            if B[i] == A[j]:
                arr[i+1][j+1] = arr[i+1-1][j+1-1]+1
            else:
                arr[i+1][j+1] = max(arr[i+1-1][j+1], arr[i+1][j+1-1])
    return arr[len(B)][len(A)]


def editDistance(source, target):
    results = []
    count = [0] * 27
    for i in range(27):
        temp = caesar(source, i)
        if temp == target:
            return 0
        results.append(temp)
        count[i] = len(set(list(temp)) & set(list(target)))

    count_max = max(count)
    Max = 0
    for i in range(len(results)):
        if count[i] == count_max:
            Max = max(LCS(results[i], target), Max)

    return 2*(len(target) - Max)


# print(editDistance('www', 'ssh'))
print(editDistance('abc', 'gzu'))
