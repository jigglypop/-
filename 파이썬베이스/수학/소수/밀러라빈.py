
import sys
sys.stdin = open("./text/15649.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

def millor_rabin(a, p):
    r = 0
    d = p - 1
    while not (d % 2):
        r += 1
        d //= 2
    x = pow(a, d, p)
    for i in range(r):
        if (x == 1 and i == 0) or x == p - 1: return True
        x = pow(x, 2, p)
    return False

result = 0
for _ in range(Int()):
    A = Int()
    flag = True
    for p in [2, 3, 5, 7, 11, 13, 17]:
        if not millor_rabin(2 * A + 1, p):
            flag = False
            break
    if flag:result += 1
print(result)