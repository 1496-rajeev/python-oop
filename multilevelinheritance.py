class A:
    name = "ravan"

class B(A):
    home  = "srilanka"

class C(B):
    def __init__(self):
        print("name is {} and he belong to {}".format(self.name, self.home))

c = C() 