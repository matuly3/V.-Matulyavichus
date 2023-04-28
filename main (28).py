n=int(input(  ))
i=0
while i<=n:
   a=1/2**i
   i=i+1
   b=1/2**i
   if i//2!=0:
       z=a+b
   else: z=a-b
   z=round(z,4)
   print(i,z)
   