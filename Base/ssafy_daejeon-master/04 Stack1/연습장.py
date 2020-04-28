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

print(memo)