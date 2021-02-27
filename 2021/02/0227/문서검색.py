import sys
import re
sys.stdin = open('1543.txt', 'r')
input = sys.stdin.readline
# words = input()
# word = input()
# print(len(re.findall(word, words)))
print(input().count(input()))
