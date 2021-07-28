credits = int(input())

if 7500 <= credits :
    print("Tera leader")
elif 6000 <= credits < 7500 :
    print("Gega leader")
elif 4500 <= credits < 6000 :
    print("Mega leader")
elif credits < 4500 :
    print("Rising Star")