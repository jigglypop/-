import sys
sys.stdin = open('펜윅트리합.txt', 'r')


def update(bit, i, plus):
    while i < len(bit):
        bit[i] += plus
        i += (i & -i)
# 갱신, i & -i는 2의 보수를 이용하여 맨 끝의 1을 찾는 연산
# 반전 후 1을 더하면 반드시 맨 마지막 1은 보존됨
# 나머지 자리는 반전했으므로 & 연산 후에 0이 됨


def sum(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= (i & -i)
    return s
# 합 구히기


input = sys.stdin.readline
n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)
# 입력

bit = [0]*(n+1)
lst = [0]
for i in range(1, n+1):
    lst.append(int(input()))
    update(bit, i, lst[i])
for i in range(0, m+k):
    q, a, b = input().split()
    q = int(q)
    a = int(a)
    b = int(b)
    if q == 1:
        update(bit, a, b-lst[a])
        lst[a] = b
    if q == 2:
        print(sum(bit, b) - sum(bit, a-1))
# 트리 구성, 0으로 차 있는 트리에 i번을 lst[i]만큼 증가시킨다
