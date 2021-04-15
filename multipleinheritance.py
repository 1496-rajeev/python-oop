class A:
    name = "ravan"
    os = "Apple"

class B: 
    name = "ram"
    website = "www.apple.com" 

class C(A,B):
    def __init__(self):
        print("this is {} operating system. contact us at {}".format(self.os,self.website))
        print("If attribute name is same in both inherite class it will print from the order first inheritated class here it is ",self.name)

a = C()