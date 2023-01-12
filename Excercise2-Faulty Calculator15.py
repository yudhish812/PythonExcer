#45*3=555, 56+9=77, 56/6=4
print("Enter the first number")
no1=int(input())
print("Enter the second number")
no2=int(input())
print("Enter the operator")
op=input()
if op=='*':
    if no1==45 and no2==3:
            print("555")
    else:
        out=no1*no2
        print(out)
elif op=='+':
    if no1==56 and no2==9:
        print("77")
    else:
        out=no1+no2
        print(out)
elif op=='/':
    if no1==56 and no2==6:
        print("4")
    else:
        out=no1/no2
        print(out)
else:
    print("check inputs")
