n=int(input())
L=[]
for _ in range(0,n):
    D=int(input())
    L.append(D)
M=pow(2,n)
for i in range(0,M):
    K=[]
    j=1
    p=0
    while j<M:
        if i&j:
            K.append(L[p])
        p+=1
        j=2*j
    print(K)