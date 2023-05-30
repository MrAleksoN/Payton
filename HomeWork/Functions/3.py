def square(sym,n,fill=True):
    line=n*sym
    if fill:
        for _ in range(n):
            print(line)
    else:
        print(line)
        for _ in range(n-2):
            print(sym+" "*(n-2)+sym)
        print(line)    
        
        
square("*",5,False)