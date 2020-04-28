# 재귀 호출
# 1. 재귀적으로 문제를 해결
# - 재귀적 정의를 코드 구현할 때
# - 좀 더 작은 문제의 해를 이용해서 좀 더 큰 문제의 해를 구하는 방법
# -> 분할정복, DP
# 2. 그래프 탐색(DFS)
# 3. 백트래킹(상태 공간 트리 탐색)
# for, while을 사용하지 않고 반복

#------------------------------------------------

# def printHello():
#     global i
#     i += 1
#     if i == 3:
#         return print('hello')
#     print('hello')
#     printHello()

#------------------------------------------------

# def printHello(i, n):
#     if i < n:
#         print(i,'hello')
#         printHello(i + 1,n)
#         print(i,'hello')

# printHello(0, 3)




# i = 0
# printHello()



#-----------------------------------------------
# def fact(n):    # n = 문제의 크기
#     if n <= 1:
#         return 1
#     return n * fact(n-1)

# print(fact(5))

print('---------------------------------------------------')
print('\t재귀')

def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)

for i in range(1, 11):
    print('fibo({}) = {}'.format(i, fibo(i)))


print('---------------------------------------------------')
print('\t재귀 + 메모')
memo = [0] * 11
memo[1] = 1

def fibo_memo(n):
    if n < 2 or memo[n]:
        return memo[n]
    memo[n] = fibo_memo(n - 1) + fibo_memo(n - 2)
    return memo[n]

fibo_memo(10)
for i in range(1, 11):
    print('memo[{}] = {}'.format(i, memo[i]))


print('---------------------------------------------------')
print('\t반복 + 메모')

memo = [0] * 11
memo[1] = 1
for i in range(2, 11):
    memo[i] = memo[i - 1] + memo[i - 2]

for i in range(1, 11):
    print('memo[{}] = {}'.format(i, memo[i]))
