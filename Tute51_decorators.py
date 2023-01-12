# def function1():
#     print("subscribe now")
#
# func2=function1
# del function1
# func2()

# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return int
# a=funcret(0)
# print(a)

# def executor(func):
#     func("this")
#
# executor(print)
def dec1(func1):
    def nowexec():
        print("Executing Now")
        func1
        print("executed Now")
    return nowexec()

def who_is_harry():
    print("A Great Boy")

who_is_harry=dec1(who_is_harry)
who_is_harry()