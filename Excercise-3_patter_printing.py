
a = int(input("enter a integer no to print pattern\n"))
print("Enter N for Normal print or R for reverse print")
b = input()
if b=="N":
    for i in range(1, a+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
else:
    for i in range(a+1,1,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()

