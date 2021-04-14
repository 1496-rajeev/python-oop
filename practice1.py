class Employee: #class define
    name = "ben"
    age = 56
    numberOfsales = 2
    def checktargetAcieved(self): #attribute called inside class using "self" key word
        if self.numberOfsales>5:
            print("target achieved")
        else:
            print("target not acheived")

employee1 = Employee() #object instance
print(employee1.name) #invoked(called) class attribute
print(employee1.checktargetAcieved())