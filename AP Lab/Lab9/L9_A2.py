class BookNotAvailable(Exception):
    pass

class InsufficientCopies(Exception):
    pass

class Book:
    def __init__(self, author, title, price, publisher, copies):
        self.author = author
        self.title = title
        self.price = price
        self.publisher = publisher
        self.copies = copies

    def __del__(self):
        print("deleting object")

    def search_title(self, title):
        if title == self.title:
            print("Author:", self.author)
            print("Title:", self.title)
            print("Price:", self.price)
        else:
            raise BookNotAvailable("Book Unavailable")

    def search_author(self, author):
        if author == self.author:
            print("Title:", self.title)
            print("No of copies available =", self.copies)
        else:
            raise BookNotAvailable("Author not found")

    def buy_no_of_copies(self, num):
        if num <= self.copies:
            print("Price of", num, "copies is", num * self.price, "\n")
        else:
            raise InsufficientCopies("Insufficient copies in stock")

books = []
B1 = Book("Prita", "Algorithms", 690, "MIT", 69)
B2 = Book("Anusha", "DBMS", 600, "MIT", 9)
B3 = Book("Khushi", "App Development", 420, "MIT", 6)
B4 = Book("Yash", "UI/UX", 90, "MIT", 60)
B5 = Book("Sara", "Everything", 1000, "MIT", 90)
B6 = Book("Arnav", "MBA Karo", 100, "MIT", 420)

books.extend([B1, B2, B3, B4, B5, B6])

ch = -1
while ch != 3:
    print("\nEnter 0 to search book using title")
    print("Enter 1 to search book using author's name")
    print("Enter 2 to check for the number of copies available")
    print("Enter 3 to exit")

    ch = int(input("Enter your choice: "))

    if ch == 0:
        title = input("Enter title: ")
        found = False
        for book in books:
            try:
                book.search_title(title)
                found = True
            except BookNotAvailable:
                pass
        if not found:
            print("Book not found")

    elif ch == 1:
        author = input("Enter author name: ")
        found = False
        for book in books:
            try:
                book.search_author(author)
                found = True
            except BookNotAvailable:
                pass
        if not found:
            print("Author not found")

    elif ch == 2:
        n = int(input("Enter the number of copies required: "))
        for book in books:
            try:
                book.buy_no_of_copies(n)
            except InsufficientCopies as e:
                print(e)

    elif ch == 3:
        print("Exiting")

    else:
        print("Invalid choice. Please enter a valid option (0-3).")
