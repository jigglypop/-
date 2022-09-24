from copy import copy, deepcopy
import re
import sys
sys.stdin = open('./text/16637.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def L(v, Args):
    if isinstance(Args, int):
        return [deepcopy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [deepcopy(v) for _ in range(Args[0])]
    return L([deepcopy(v) for _ in range(Args.pop())], Args)

N = Int()
word = Str()
P = re.findall("[+|*|-]", word)
nums = list(map(int, re.findall("[0-9]", word)))
Max = - (2 ** 31 + 1)
calc = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "-": lambda x, y: x - y
}
print(Max)
for i in range(1 << len(P)):
    S = []
    print(int(2, i)[2:])