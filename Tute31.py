with open("yudhi.txt") as f:
    print(f.readline())
    print(f.tell())
    a=f.tell()
    print(a)

f=open("yudhi.txt","rt")
print(f.readline())
f.close()