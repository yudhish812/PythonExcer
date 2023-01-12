class Employee:
    No_of_leaves=8
    basketball=1
    _age=13
    __game=36
    def __init__(self,n,s,r):
        self.name=n
        self.salary=s
        self.role=r
    @classmethod
    def change_leaves(cls, leaves):
        cls.No_of_leaves=leaves
    @classmethod
    def from_str(cls, string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    @staticmethod
    def hell(strings):
        print("This is illustration of static method"+strings)
        return 89
emp=Employee("Yudhi",748,"Coder")
print(emp._Employee__game)