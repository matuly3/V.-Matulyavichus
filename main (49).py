x = int(input())
if x > 99 and x < 999:
    a = x % 10
    b = x // 10 % 10
    c = x // 100 % 10
    y=str(a)+str(b)+str(c)
    y=int(y)
print(x-y)
