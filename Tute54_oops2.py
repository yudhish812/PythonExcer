class Employee:
    No_of_leaves=8
    pass
harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=455
harry.role="Instructor"

rohan.name="Rohan"
rohan.salary=4554
rohan.role="Coder"
# Employee.No_of_leaves=10
rohan.No_of_leaves=9
print(Employee.__dict__)
# print(harry.__dict__)
# print(harry.No_of_leaves)