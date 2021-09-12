import sys
sys.stdin = open('1094.txt', 'r')
print(bin(int(input()))[2:].count('1'))