import sys
sys.stdin = open('9536.txt', 'r')
T = int(input())
for _ in range(T):
    words = list(map(str, input().split()))
    remove_set = set()
    while True:
        target = list(map(str, input().split()))
        if target == ['what', 'does', 'the', 'fox', 'say?']:
            break
        remove_set.add(target[-1])
    for word in words:
        if word not in remove_set:
            print(word, end=' ')
