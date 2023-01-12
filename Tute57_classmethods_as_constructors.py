class Employee:
    No_of_leaves=8
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


yudhi=Employee("Yudhi",234,"AP")
karan=Employee.from_str("Karan-480-student")
yudhi.change_leaves(36)
print(Employee.No_of_leaves)
print(yudhi.salary)
print(karan.salary)