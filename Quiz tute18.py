while(1):
    print("Enter the number")
    no=input()
    if int(no)<100:
        continue
    if int(no)>100:
        print("Congratulations", no)
        break
