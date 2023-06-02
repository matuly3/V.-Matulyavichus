def bank():
    a = int(input("Размер вклада "))
    years = int(input("На сколько лет "))
    p = a*(1+0.1)**years
    print(p)
bank()
    
