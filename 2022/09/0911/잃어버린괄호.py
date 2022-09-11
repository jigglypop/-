from pprint import pprint
import re
import sys
sys.stdin = open('./text/1541.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

words = Str()
words_minus = words.split("-")
S = []
for plus_words in words_minus:
    S.append(sum(list(map(int, plus_words.split("+")))))
result = S[0]
S = S[1:]
for s in S:
    result -= s
print(result)