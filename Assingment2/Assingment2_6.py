def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)
a = int(input())
b = int(input())
if(gcd(a, b)<0):
    print(-1*(gcd(a, b)))
else:
    print(gcd(a, b))