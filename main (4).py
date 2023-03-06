import math
a = int(input())
b = int(input())
if a > 0 and b > 0:
    print((a+b)/2)
    x = math.sqrt(a * b)
    print(x)
else:
    print("Wrong Numbers")
