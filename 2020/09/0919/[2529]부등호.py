import sys
sys.stdin = open('2529.txt', 'r')

result = []
N = int(input())
blank = list(map(str, input().split()))
result = []


def perm(k, chosen, visited):
    if k == N:
        result.append(chosen[::])
        return
    for i in range(10):
        if (1 << i) & visited:
            continue
        if blank[k] == '<' and chosen[-1] < i:
            chosen.append(i)
            perm(k+1, chosen, visited | (1 << i))
            chosen.pop()
        if blank[k] == '>' and chosen[-1] > i:
            chosen.append(i)
            perm(k+1, chosen, visited | (1 << i))
            chosen.pop()


for i in range(10):
    perm(0, [i], 0 | (1 << i))
results = []
for r in result:
    temp = ''
    for i in r:
        temp += str(i)
    results.append(temp)

print(results[-1])
print(results[0])
