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
        # You should not print "Not Present" here to continue searching other books.

    def search_author(self, author):
        if author == self.author:
            print("Title:", self.title)
            print("No of copies available =", self.copies)
        # You should not print "Not Present" here to continue searching other books.

    def buy_no_of_copies(self, num):
        if num <= self.copies:
            print("Price of", num, "copies is", num * self.price)
        else:
            print("Required Copies not in Stock")

books = []
B1 = Book("Aditya", "Algorithms", 690, "MIT", 69)
B2 = Book("Anurag", "DBMS", 600, "MIT", 9)
B3 = Book("Praveen", "App Development", 420, "MIT", 6)
B4 = Book("Akshay", "UI/UX", 90, "MIT", 60)
B5 = Book("Aniket", "Everything", 1000, "MIT", 90)
B6 = Book("Abhay", "MBA Karo", 100, "MIT", 420)

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
            book.search_title(title)
            found = True
        if not found:
            print("Not Present")

    elif ch == 1:
        author = input("Enter author name: ")
        found = False
        for book in books:
            book.search_author(author)
            found = True
        if not found:
            print("Not Present")

    elif ch == 2:
        n = int(input("Enter the number of copies required: "))
        for book in books:
            book.buy_no_of_copies(n)

    elif ch == 3:
        print("Exiting")

    else:
        print("Invalid choice. Please enter a valid option (0-3).")
