def mir(n):
    mil=[2,7,61]
    if n in mil:
        return 1
    if (n%2==0) or (n==1):
        return 0
    r=0
    s=n-1
    while not s%2 and s:
        r+=1
        s=s//2
    def gom(a):
        x=pow(a,s,n)
        if x==1 or x==n-1:
            return 0
        for _ in range(r):
            x=pow(x,2,n)
            if x==n-1:
                return 0
        return 1
        
    for a in mil:
        if gom(a):
            return 0
    return 1

cnt=0
for _ in range(int(input())):
    if mir(int(input())*2+1):
        cnt+=1
print(cnt)