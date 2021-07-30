n=int(input())
K=0
for i in range(0,n):
    D=int(input())
    if(D%5==0):
        K+=1
print(K)