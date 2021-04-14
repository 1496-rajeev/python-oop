class Employee:
    def meth1(self): #instance method
        self.name = "ravan"
        print("instance method", self.name)
     
    @staticmethod # decorator
    def meth2(): #static method without use of "self"
        print("static method")

employee = Employee()
employee.meth1()
employee.meth2()