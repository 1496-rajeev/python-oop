class Library:
    def __init__(self, booklist):
        self.booklist= booklist

    def availableBook(self):
        print("Available books: ")
        for books in self.booklist:
            print(books)

    def borrowBook(self, requestBook):
        if requestBook in self.booklist:
            print("You borrow ",requestBook)
            self.booklist.remove(requestBook)
        else:
            print("sorry!", requestBook ,"is not available")

    def addreturnBook(self,returnBook):
        self.booklist.append(returnBook)
        print("tank you! you retun ", returnBook)
        pass

class Customer:
    def returnBook(self):
        print("Enter retun book name ")
        self.bookname = input()
        return self.bookname
    
    def requestBook(self):
        print("Enter book name to take ")
        self.bookname = input()
        return self.bookname 

library = Library(["math", "science", "english"])
customer = Customer()

while True:
    print("Enter 1 for available books")
    print("Enter 2 to borrow books")
    print("Enter 3 to return books")
    print("Enter 4 to exit")
    userinput = int(input())
    if userinput == 1:
        library.availableBook()
    elif userinput == 2:
       requestedbook = customer.requestBook()
       library.borrowBook(requestedbook)
    elif userinput == 3:
       returnbook = customer.returnBook()
       library.addreturnBook(returnbook)
    elif userinput == 4:
        quit()


