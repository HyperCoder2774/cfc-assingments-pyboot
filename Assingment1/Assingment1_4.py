def func(a):
    if a==0:
        return 2;
    return func(a-1)+4*a
a=int(input())
if (a>0):
    print(func(a-1))