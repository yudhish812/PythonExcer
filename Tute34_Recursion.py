# def factorial_iterative(n):
#     for i in range(n-1):
#         n=n*(i+1)
#     return n
#
# n=int(input("enter the number"))
# print(factorial_iterative(n))

#recursive method

def factorial_recursive(n):
    if n==0:
        return 1
    else:
        fac = n
        fac = fac * factorial_recursive(n - 1)
        return fac

n=int(input("Enter the number"))
print(factorial_recursive(n))

