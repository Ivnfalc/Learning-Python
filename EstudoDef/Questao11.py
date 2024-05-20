def result(i):
    n = int(input("digite numero:"))
    while n > 100:
        n = n + 1
    
    print (n)
    n = int(input("digite numero:"))
    return n 
    
i = result
n = i
print(result(n))
print(n*2 )
