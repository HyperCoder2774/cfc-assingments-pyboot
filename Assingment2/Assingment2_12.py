def swap(i,j,L):
    L[i],L[j]=L[j],L[i]
n=int(input())
L=[]
for _ in range(0,n):
    D=int(input())
    L.append(D)
for i in range(0,n):
    if(L[i]%2):
        for j in range(i,n):
            if(L[j]%2==0):
                swap(i,j,L)
print(L)