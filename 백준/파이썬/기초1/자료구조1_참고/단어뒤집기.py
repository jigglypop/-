import sys
from pprint import pprint
sys.stdin = open('9093.txt', 'r')
input = sys.stdin.readline
for _ in range(int(input())):
    words = map(lambda x: x[::-1], input().split())
    print(*words)
