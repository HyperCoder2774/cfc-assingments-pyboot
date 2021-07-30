def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)
a=int(input())
b=int(input())
if a==0 or b==0:
    print("The LCM of zero does not exist. Remove 0's and try again.")
else:
    if (a < 0):
        a = -1 * a
    if (b < 0):
        b = -1 * b
    print((a * b) / gcd(a, b))