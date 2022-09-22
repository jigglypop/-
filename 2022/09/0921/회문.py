from copy import copy, deepcopy
import sys
sys.stdin = open('./text/17609.txt', 'r')
input = sys.stdin.readline
def Int():return int(input().strip())
def Str():return input().strip()

def is_palindrome(word):
    l, r = 0, len(word) - 1
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            if l + 1 < r:
                R = word[:r] + word[r + 1:]
                L = word[:l] + word[l + 1:]
                if R[:] == R[::-1] or L[:] == L[::-1]:
                    return 1
                else:
                    return 2
    return 0

for _ in range(Int()):
    print(is_palindrome(Str()))