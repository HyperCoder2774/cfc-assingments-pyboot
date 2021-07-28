def a(x):
    for i in range(1,x+1):
        print(i*"* ")
def b(x):
    for i in range(1, x + 1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
def c(x):
    for i in range(1,x+1):
        k=i-1
        print((x-i)*"  ",end="")
        for j in range(1,i+1):
            print(j,end=" ")
        while k:
            print(k, end=" ")
            k=k-1
        print()
def d(x):
    for i in range(1, x + 1):
        print((x - i) * "  ", end="")
        for j in range(i,2*i):
            print(j, end=" ")
        j=2*(i-1)
        while j>=i:
            print(j,end=" ")
            j=j-1
        print()
def e(x):
    for i in range(1, x + 2):
        c=1
        for j in range(1, i + 1):
            print(c, end=" ")
            c = c * (i - j) // j
        print()
def f(x):
    for i in range(1, x + 1):
        print((x - i) * "  ", end="")
        print((2*i-1)*"* ")
    for i in range(1,x):
        print(i*"  ",end="")
        print((2*(x-i)-1)*"* ")
def g(x):
    for i in range(1, x + 1):
        print(i*"* ",end="")
        print((2*(x-i))*"  ",end="")
        print(i * "* ")
    for i in range(1, x):
        print((x-i)*"* ",end="")
        print((2*i)*"  ",end="")
        print((x - i) * "* ")
def h(x):
    print((2*x-1)*"* ");
    for i in range(1,x):
        print((x-i)*"* ",end=" ")
        print((4*i-3)*" ",end="")
        print((x-i)*"* ")
    j=x-1
    while j:
        print((x - j) * "* ", end=" ")
        print((4 * j - 3) * " ", end="")
        print((x - j) * "* ")
        j=j-1
    print((2 * x - 1) * "* ");
def i(x):
    k=2*x-1
    for i in range(0,x):
        a=x
        while a>x-i:
            print(a,end=" ")
            a=a-1
        print((k-2*i)*f'{x-i} ',end="")
        a=x-i+1
        while a<=x:
            print(a, end=" ")
            a = a + 1
        print()
    i=x-2
    while i>=0:
        a = x
        while a > x - i:
            print(a, end=" ")
            a = a - 1
        print((k - 2 * i) * f'{x - i} ', end="")
        a = x - i + 1
        while a <= x:
            print(a, end=" ")
            a = a + 1
        print()
        i=i-1
x=int(input())
a(x)
b(x)
c(x)
d(x)
e(x)
f(x)
g(x)
h(x)
i(x)