
import sys
sys.stdin = open('./text/11479.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def Str():return input().strip()
