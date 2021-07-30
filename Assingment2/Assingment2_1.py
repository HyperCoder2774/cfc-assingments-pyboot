def Dectoc(x):
    s=""
    while x:
        rem = x % 8;
        x = x // 8;
        s=str(rem)+s
    return s

n=int(input())
print(Dectoc(n))