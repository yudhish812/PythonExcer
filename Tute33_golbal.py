
# l=10 #Global Variable
# def function1(n):
#     l=5 #localvaribles
#     m=8  #localvaribles
#     print(n)
#     # print(l, m)
#     c=sum((l,m))
#     return c
#
# print(l)
# print(function1(2))

# l=10 #Global Variable
# def function1(n):
#     m=8  #localvaribles
#     print(n)
#     # print(l, m)
#     global l
#     l=l+20
#     c=sum((l,m))
#     return c
#
# print(l)
# print(function1(2))
x=2
def Yudhi():
    x=34
    print(x)
    def champ():
        global x
        x=x+5
        print(x)
        return 2
    return 3
    print(champ())

print(Yudhi())






