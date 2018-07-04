import sys;
import os;
from BookHelper import BooksHelper
msg = """

---------------------------------------------------------
Welcome to Book Place MAnagement
---------------------------------------------------------

1. Add New Book Entry
2. Search Book
3. Modify Book Entry
4. Delete Book Entry
5. View All Books
6. Exit From the Menu

"""
b = BooksHelper()
while 1:
    print(msg)
    try:
        choice = input("Enter Your Choice: ")
        option = int(choice) 
    except:
        print("Invalid Otion Entered..")
        raw_input("Press any key to continue")
        os.system("clear")
    else:
        if option == 6:
            sys.exit()
        elif option == 1:
            b.addNewBook()
        elif option == 2:
            searchString = input("Enter search String: ")
            b.searchBook(searchString)
        elif option==3:
            isbn_no = input("Enter ISBN Number: ")
            b.modifyBookEntrybyIsbn(isbn_no)
        elif option == 4:
            isbn_no = input("Enter ISBN Number: ")
            b.deleteBookEntry(isbn_no)
        elif option == 5:
            b.viewAllBooks()
        else:
            print("Invalid Input")
            input("Press any key to continue")
