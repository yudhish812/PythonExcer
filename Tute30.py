f=open("yudhi.txt")
print(f.tell())
print(f.readline(), end="")
print(f.tell())
f.seek(5)
print(f.readline())
print(f.tell())
print(f.readline())
f.close()