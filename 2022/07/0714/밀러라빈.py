
import sys
sys.stdin = open("./text/5615.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

def millor_rabin(n):
    for p in [2, 3, 5, 7, 11, 13, 17]:
        r = 0
        d = n - 1
        while not (d % 2):
            r += 1
            d //= 2
        x = pow(p, d, n)
        flag = False
        for i in range(r):
            if (x == 1 and i == 0) or x == n - 1:
                flag = True
                break
            x = pow(x, 2, n)
        if not flag: return False
    return True
    
result = 0
for _ in range(Int()):
    A = Int()
    flag = millor_rabin(2 * A + 1)
    print(2 * A + 1, flag)
    if flag:result += 1
print(result)