import sys

def subset(k,N):
    if k == N:      
        print(bits)
        return 
    bits[k] = 0
    subset(k+1,N)
    bits[k] = 1
    subset(k+1,N)
    
sys.stdin = open('input2.txt','r')
N, M = map(int,sys.stdin.readline().split()) 
m = [i for i in range(1,N+1)]
bits = [0] * N

subset(0,N)
print(r)