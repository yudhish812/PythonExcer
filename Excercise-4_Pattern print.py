a=int(input("Eneter no of rows"))
b=input("Enter N for Normal Pattern and any key for reverse Pattern")
if b=="N":
    for i in range(1,a+1):
        print("*"*i)
else:
    for i in range(a+1,1,-1):
        print("*"*i)
