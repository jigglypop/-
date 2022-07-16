
import sys
sys.stdin = open('./text/2252.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def Str():return input().strip()


def merge(arr):
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    L = merge(arr[:m])
    H = merge(arr[m:])
    nums = []
    l = h = 0
    while l < len(L) and h < len(H):
        if L[l] < H[h]:
            nums.append(L[l])
            l += 1
        else:
            nums.append(H[h])
            h += 1
    nums += L[l:]
    nums += H[h:]
    return nums

print(merge([1,4,3,4,2]))