from math import cos, sin, pi
import sys
sys.stdin = open("./text/10531.txt", "r")
from math import pi,sin,cos
def FFT(X,inv=False):
    n,j=len(X),0
    for i in range(1,n):
        bit=n>>1
        while j>=bit:
            j-=bit
            bit>>=1
        j+=bit
        if i<j:
            X[i],X[j]=X[j],X[i]
    d=2
    while d<=n:
        ang=2*pi/d
        if inv: ang=-ang
        dw=cos(ang)+sin(ang)*(1j)
        for i in range(0,n,d):
            w=1
            for j in range(d//2):
                u,v=X[i+j],X[i+j+d//2]*w
                X[i+j],X[i+j+d//2]=u+v,u-v
                w*=dw
        d<<=1
    if inv:
        for i in range(n):
            X[i]/=n
    return X
N=1<<19
A=[0]*N
for i in range(int(input())):
    A[int(input())]=1
A[0]=1
B=[0]*200001
for i in range(int(input())):
    B[int(input())]+=1
FFT(A)
A=[i*i for i in A]
FFT(A,True)
A=[round(abs(i)) for i in A]
print(sum(A))
ans=0
for i in range(200001):
    if B[i]>0 and A[i]>0:
        ans+=B[i]
print(ans)