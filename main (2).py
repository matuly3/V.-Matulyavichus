x = int(input())
if x > 999 and x < 10000:
   a = x % 10
   b = x // 10 % 10
   c = x // 100 % 10
   d = x // 1000
   print(a+b+c+d)
   print(a*b*c*d)
else: 
   print("Wrong Number")
 