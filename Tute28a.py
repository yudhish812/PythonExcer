# f=open("Yu1.txt","w")
# f.write("Champ Bro")
# f.close()
# f=open("Yu1","a")
# a=f.write("append\n")
# print(a)
# f.close()

# f = open("Yu1.txt","r")
# # f.write("Whatever")
# print(f.read())
# f.close()

# print(f.read())
# f.write("checking")
# f.close()

f = open("Yu1.txt", "r+")
print(f.read())
f.write("\ncheck")
print(f.read()) #f.read() command reads only already existing content. f.write() can write infile.
f.close()

