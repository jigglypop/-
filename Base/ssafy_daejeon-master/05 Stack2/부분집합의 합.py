import sys

sys.stdin = open('input.txt','r')
def subset(k,n):
    if k == n:
        r = []        
        for i in range(n):
            if bits[i]:
                r.append(m[i])
        return R.append(r)
    bits[k] = 0
    subset(k+1,n)
    bits[k] = 1
    subset(k+1,n)

T = int(input())
for tc in range(1,T+1):
    n,s = map(int,input().split())
    bits = [0] * 12
    m = [i for i in range(1,13)]
    R = []    
    subset(0,12)
    a = 0
    for i in range(1,len(R)):
        if len(R[i]) == n and sum(R[i]) == s:            
            a = 1
    print('#{} {}'.format(tc,a))
    
    
