print("Введите значение в м/c")
a = float(input())
print("Введите значение в км/ч")
b = float(input())
x = b / 3.6
if a > x:
    print("Значение в м/c больше")
elif a < x:
    print("Значение в км/ч больше")
else:
    print("Значения равны")
