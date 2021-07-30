n=int(input())
target=int(input())
L=[]
for _ in range(0,n):
    D=int(input())
    L.append(D)
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j + 1, n):
            if (L[i] + L[j]+L[k] == target):
                print(f'({L[i]},{L[j]},{L[k]})')