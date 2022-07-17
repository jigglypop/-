from pprint import pprint
import sys
sys.stdin = open('./text/1026.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def List():return list(map(int, input().strip().split()))

N = Int()
A = List()
B = List()
A.sort()
B.sort(reverse=True)
print(sum([i * j for i, j in zip(A, B)]))