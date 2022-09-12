from math import sqrt, pow
import sys
sys.stdin = open('./text/1789.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
print(int((-1 + (sqrt(pow(1, 2) + 8 * N))) / 2))

