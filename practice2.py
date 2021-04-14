class Employee:
    workinghour = 45

employee1 = Employee() # created employee object
employee2 = Employee()# created employee object
print(employee1.workinghour)
print(employee2.workinghour)
Employee.workinghour = 29 # changed attribute value of class
print(employee1.workinghour)
print(employee2.workinghour)
employee1.workinghour = 4 # changed attribute value for one object
print(employee1.workinghour)
print(employee2.workinghour)
Employee.name = "ravan" # created new attribute in class
print(employee1.name)
print(employee2.name)
employee1.name = "ram"
print(employee1.name)
print(employee2.name)


