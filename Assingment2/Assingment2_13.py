def swap(i,j,L):
    L[i],L[j]=L[j],L[i]
n=int(input())
L=[]
for _ in range(0,n):
    D=int(input())
    L.append(D)
l=0
r=n-1
while l<=r:
    swap(l,r,L)
    l=l+1
    r=r-1
print(L)