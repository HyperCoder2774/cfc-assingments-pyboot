def func(a):
    i=0
    while (a):
        a=a//10
        i=i+1
    return i
a=int(input())
if a>0:
    print(func(a))
elif a==0:
    print(1)
else:
    print(func(-1*a))