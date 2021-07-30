def prime(x):
    for i in range(2,x):
        if(x%i==0):
            return 0;
    return 1;

n=int(input())
K=0
for i in range(0,n):
    D=int(input())
    if(prime(D)):
        K+=1
print(K)