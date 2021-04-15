class Apple:
    brandname = "Apple inc."
    website = "www.aplle.com"

    def contactDetail(self):
        print("Contact us at", self.website)

class Macbook(Apple):
    manufYear = 2021
    def productDetail(self):
        print("This is created by {} in {}".format(self.brandname,self.manufYear))

macbook = Macbook()
macbook.productDetail()
macbook.contactDetail()