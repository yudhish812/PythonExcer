




def fabbonacci_series(n):
    a = 0
    b = 1
    if n==1:
        return 0
    elif n==2:
        c=a+b
        return c
    else:
        fab=fabbonacci_series(n-1)+fabbonacci_series(n-2)
        return fab

n=int(input("Enter the number of terms"))

print(fabbonacci_series(n))

