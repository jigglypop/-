import sys
from collections import deque
sys.stdin = open("11728.txt", "r")
input()
print(' '.join(sorted(sys.stdin.read().split(), key=int)))
