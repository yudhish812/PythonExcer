def getdate():
    import datetime
    return datetime.datetime.now()


f1=open("Ram_food.txt", "r+")
# f1.write("Roti")
print(getdate(),"\n",f1.read())

f1.close()
f2=open("Shyam_food.txt", "w")

f2.close()

f3=open("Mohan_food.txt", "w")


f3.close()
f4=open("Ram_exc.txt", "w")

f4.close()
f5=open("Shyam_exc.txt", "w")

f5.close()
f6=open("Mohan_exc.txt", "w")

f6.close()