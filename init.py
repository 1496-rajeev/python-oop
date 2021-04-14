class Employee:
    def __init__(self,passedName): #this method called(invoke) when class or object is called
        self.name = passedName

    def showName(self):
        print(self.name)

employee1 = Employee("ravan")
employee2 = Employee("ram")

employee1.showName()
employee2.showName()