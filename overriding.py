class A:
    def meth1(self):
        self.value = 40
        print(self.value)

class B(A):
    def meth1(self): # overriding method of base class
        self.value = 35 
        print(self.value)
    
    def meth2(self): # getting value of base class after overriding
        super().meth1()


a=A()
a.meth1()
b = B()
b.meth1()
b.meth2()