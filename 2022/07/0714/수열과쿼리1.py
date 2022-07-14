
import sys
sys.stdin = open('./text/13537.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
INF = sys.maxsize
N = Int()
board = Split()
M = Int()

