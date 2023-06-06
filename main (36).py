def q():
    x = int(input("Введите четырехзначное число " ))
    if x > 999 and x < 10000:
         a = x % 10
         b = x // 10 % 10
         c = x // 100 % 10
         d = x // 1000 % 10
         e = a*b*c*d
         f = a+b+c+d
         print(f)
         print(e)
    else:
         print("Введите четырехзначное число!")
q()
def w():
    x = int(input("Введите пятизначное число "))
    if x > 9999 and x < 100000:
         a = x % 10
         b = x // 10 % 10
         print(a)
         print(b)
    else:
        print("Введите пятизначное число !!! ")
w()
def e():
    x = int(input('Введите трёхзначное число '))
    if x > 99 and x < 1000:
         a = x % 10
         b = x // 10 % 10
         c = x // 100 % 10
         v=str(a)+str(b)+str(c)
         d = x - int(v)
         print(d)
    else:
        print("Введите трёхзначное число!!!")
e()
def r():
    x = (input("Введите целое число "))
    for i in x:
        print(i)
r()
def t():
    x = (input())
    z=[]
    for i in x:
        z.append(i)
    if str(2) in z:
        print("есть")
    else: print("нет")
t()
    
    