#public = memberName
#protected = _memberName
#Private = __memberName

class Car:
    weels = 4
    _color = "black" #call within class or inheritate class
    __year = 2021 # call within class

class Bmw(Car):
    def __init__(self):
        print("protected Attribute {} calling private {}".format(self._color, self.__year))

car = Car()
print("public attribute number of weels {}".format(car.weels))
