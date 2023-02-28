x = int(input())
if x > 9999 and x < 100000:
   a = x % 10
   b = x // 10 % 10
   c = x // 100 % 10
   d = x // 1000 % 10
   e = x // 10000 % 10
   print(a)
   print(b)
else:
   print("Wrong Number")