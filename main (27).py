n=int(input(  ))
i=1
while i<=n:
    s=(2*i-1)/(2*i)
    i=i+1
    z=(2*i-1)/(2*i)
    p=z+s 
    p=round(p,4)
    print(i,p)