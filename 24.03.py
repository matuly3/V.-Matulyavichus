print("Введите год")
a = int(input())
if 0<a<1000:
    if a%400 == 0:
        print("Год високосный")
    else:
        print("Год не високосный")
elif a%4 == 0:
    print("Год високосный")
else:
    print("Год не високосный")