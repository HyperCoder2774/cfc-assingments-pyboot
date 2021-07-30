n=input()
L=[]
for i in range(0,len(n)):
    L.append([n[i],str(i+1)]);
L.sort()
S=""
for i in range(0,len(n)):
    S+=L[i][1]
print(S)