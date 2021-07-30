n=int(input())
L=[]
A=[]
Ds=[]
for i in range(0,n):
    D=int(input())
    L.append(D)
    A.append(D)
    Ds.append(D)
A.sort()
Ds.sort(reverse=True)
r1=1
for i in range(0,n):
    if(L[i]!=A[i]):
        r1=0
        break
r2=1
for i in range(0,n):
    if(L[i]!=Ds[i]):
        r2=0
        break
if r1 or r2:
    print("Sorted")
else:
    print("Not Sorted")