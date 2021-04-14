class Employee:
    age =20
    def meth1(self):
        self.name = "ravan"
        age = 40
        print("meth1 name ", self.name) # with "self" attribute available for the life of the class
        print("meth1 age ", age) #witjout "self" attribute is valid only inside the method

    def meth2(self):
        print("called meth2")
        print("meth1 name ", self.name)
        print("meth1 age ", self.age) # error because it is define in only meth1

employee = Employee()
employee.meth1() # this is same as "Employee.meth1(employee)"
employee.meth2()
