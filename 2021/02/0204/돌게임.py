import sys
from pprint import pprint

sys.stdin = open('9655.txt', 'r')
print('SK' if int(input()) % 2 == 1 else 'CY')
