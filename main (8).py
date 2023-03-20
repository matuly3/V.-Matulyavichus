print("Введите сторону квадрата")
a = float(input())
print("Введите радиус круга")
b = float(input())
c = a**2
d = b**2
if c > d:
    print("Площадь квадрата больше")
elif c < d:
    print("Площадь круга больше")
else:
    print("Площади Равны")
