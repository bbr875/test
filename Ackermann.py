def Ackermann(m,n):
    if m==0:
        return n+1
    elif n==0:
        return Ackermann(m-1,1)
    else:
        return Ackermann(m-1, Ackermann(m,n-1))

x=list(map(int,input().split()))
print(Ackermann(x[0],x[1]))