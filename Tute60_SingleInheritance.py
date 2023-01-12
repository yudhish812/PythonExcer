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
    @staticmethod
    def hell(strings):
        print("This is illustration of static method"+strings)
        return 89

class programmer(Employee):
    def __init__(self,n,s,r,l):
        self.name = n
        self.salary = s
        self.role = r
        self.languages=l
    def printprog(self):
        print(f"Name is {self.name}, salary is {self.salary},role is {self.role},and language {self.languages}")
yudhi=Employee("Yudhi",235,"Student")
bantu=Employee("Omjee",210,"student")

anshul=programmer("Snehil",430,"Product Manager","Python")
raj=programmer("Raj",410,"Sales","C")
print(raj.printprog())
