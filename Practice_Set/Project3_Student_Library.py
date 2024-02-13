class Student:
    def Borrow_Book(self):
        print("Enter the book name:")
        book_name=input()

        if book_name.lower() in Library.Books:
            print("Book borrowed successfully")
        else:
            print("Book is not available")

class Library:
    Books=["physics","chemistry","biology","english","machine learning","ai","python"]

    def Display_Books(self):
        print("Books avaailable in the library are:")
        for i in range(0,len(Library.Books),1):
            print(Library.Books[i])

def main():
    print("Welcome to Student Library Management System!!!\n")

    lib=Library()
    lib.Display_Books()
    
    std=Student()
    std.Borrow_Book()

if __name__=="__main__":
    main()