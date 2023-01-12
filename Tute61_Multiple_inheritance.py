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

class player:
    no_of_games=4
    def __init__(self,n,g):
        self.name=n
        self.game=g
    def printdetails(self):
        return f"Name is {self.name}, He plays {self.game}"
class coolprogrammer(Employee, player):
    pass


sunil=coolprogrammer("Sunil",233,"Excel")
print(sunil.printdetails())

