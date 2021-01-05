def convert(q, base):
    w = '0123456789ABCDEF'
    re = ''
    while q > 0:
        q, r = divmod(q, base)
        re = w[r] + re
    return re

def solution(n, t, m, p):
    answer = ''
    numbers = '0'
    i = 0
    while len(numbers) < t * m+1:
        numbers += convert(i,n)
        i += 1
    idx = [i-1 for i in range(p,len(numbers),m)]
    for i in idx:
        answer += numbers[i]
    return answer
solution(2,4,2,1)




