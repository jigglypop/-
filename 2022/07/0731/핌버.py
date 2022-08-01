import sys
sys.stdin = open('./text/16877.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

fib = [1,2]
pimber = [0]
while fib[-1] < 3100000:
    fib.append(fib[-1] + fib[-2])
for i in range(1, 3000001):
    j = 0
    cnt = [0] * 34
    while fib[j] <= i:
        if pimber[i - fib[j]] <= 33:
            cnt[pimber[i - fib[j]]] += 1
        j += 1
    for i in range(34):
        if cnt[i] == 0:
            break
    pimber.append(i)
N = Int()
word = List()
result = 0
for w in word:
    result ^= pimber[w]
print("koosaga" if result else "cubelover")