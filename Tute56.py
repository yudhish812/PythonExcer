class Employee:
    No_of_leaves=8
    def __init__(self,n,s,r):
        self.name=n
        self.salary=s
        self.role=r
    @classmethod
    def change_leaves(cls, leaves):
        cls.No_of_leaves=leaves

yudhi=Employee("Yudhi",234,"AP")
yudhi.change_leaves(36)
print(Employee.No_of_leaves)
print(yudhi.salary)