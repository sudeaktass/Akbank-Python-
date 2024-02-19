class Library:
    def __init__(self, book_name="", author="", release_date="", num_pages="", file="books.txt"):
        self.book_name = book_name
        self.author = author
        self.release_date = release_date
        self.num_pages = num_pages
        self.file = file
        print("Book saved")

    def list_books(self):
        file = open("file", "a")

        with open(self.file, "r") as file:
            for line in file:
                book_information = line.strip().split(",")
                print(f"Book: {book_information[0]}, Author: {book_information[1]}")



    def add_book(self):
        book_name = input("The book title: ")
        author = input("The author's name: ")
        release_date = int(input("The release date: "))
        num_pages = int(input("The number of pages: "))

        with open(self.file, "a") as file:
            file.write("{},{},{},{}\n".format(book_name, author, release_date, num_pages))
        print("Book saved.")

    def remove_book(self):
        remove_title = input("Book title to be removed: ")
        book = []
        with open(self.file, "r") as file:
            for line in file:
                if remove_title not in line:
                    book.append(line)
        with open(self.file, "w") as file:
            for line in book:
                file.write(line)


lib = Library()

while True:
    print("""
            *** MENU ***
            1) List Books
            2) Add Book
            3) Remove Book 
            4) Exit
                   """)
    command = input("Enter your choice: ")

    if command == "1":
        lib.list_books()
    elif command == "2":
        lib.add_book()
    elif command == "3":
        lib.remove_book()
    elif command == "q":
        print("Exiting.")
        break
    else:
        print("Invalid choice. Try again.")