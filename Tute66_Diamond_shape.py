class A:
    def meth(self):
        print("This is in class A")

class B(A):
    def meth(self):
        print("This is in class B")

class C(A):
    def meth(self):
        print("This is in class C")

class D(B,C):
    def meth(self):
        print("This is in class D")

a=A()
b=B()
c=C()
d=D()
d.meth()