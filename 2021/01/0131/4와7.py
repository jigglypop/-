import sys
sys.stdin = open("2877.txt", 'r')

print(bin(int(input())+1)[3:].translate(''.maketrans('01', '47')))
