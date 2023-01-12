class Employee:
    No_of_leaves=8
    def __init__(self,n,s,r):
        self.name=n
        self.salary=s
        self.role=r
    pass

yudhi=Employee("Yudhi",234,"AP")
print(yudhi.salary)