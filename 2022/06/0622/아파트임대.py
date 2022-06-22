import sys
sys.stdin = open("./text/5615.txt", "r")
input = sys.stdin.readline

def mir(n):
    prime = [2,7,61]
    if n in prime:
        return True
    if n % 2 ==0 or n == 1:
        return False
    r = 0
    s = n-1
    while not s%2 and s:
        r += 1
        s = s//2

    def calc(a):
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r):
            x = pow(x, 2, n)
            if x == n-1:
                return False
        return True
        
    for a in prime:
        if calc(a):
            return False
    return True

cnt=0
for _ in range(int(input())):
    if mir(int(input())*2+1):
        cnt+=1
print(cnt)