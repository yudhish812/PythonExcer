class A:
    classvar1="Im class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.classvar1="Instance varible of A"
        self.spe="special"

class B(A):
    classvar1="I am in class B"
    def __init__(self):
        self.var1="I am inside class B's constructor"
        self.classvar1="Instance varible of B"
        super().__init__()

a=A()
b=B()
print(b.spe,b.classvar1,b.var1)
