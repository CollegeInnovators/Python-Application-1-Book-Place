import os
import sys
import pickle
class BooksHelper:
    dbFileName = "dbfile.txt"
    def __init__(self):
        if os.path.exists(BooksHelper.dbFileName):
             pass
        else:
            print("Initializing the database file...")
            try:
                f = open(BooksHelper.dbFileName,"w")
                f.close()
            except:
                print("Failed to Initialize db File...")
                sys.exit();

    def getFileSize(self):
        return os.path.getsize(BooksHelper.dbFileName)

    def addNewBook(self):
        isbn_number = input("Enter The ISBN number: ");
        book_title = input("Enter Book Title: ");
        author_name = input("Enter the Author Name: ");
        location = input("Enter Location: ")

        if self.getFileSize()>0:
            print("Adding new entry...")
            #add book method
            self.addBook(isbn_number, book_title, author_name, location)
        else:
            f =open(BooksHelper.dbFileName,"wb")
            tempDict={}
            pickle.dump(tempDict,f)
            f.close()
            #add book method
            self.addBook(isbn_number, book_title, author_name, location)


    def addBook(self, isbn_number,book_title,author_name, location):
        f =open(BooksHelper.dbFileName,"rb")
        tempDict = pickle.load(f)
        f.close()
        f =open(BooksHelper.dbFileName,"wb")
        tempDict[isbn_number] = [isbn_number,book_title,author_name, location]
        print( "Adding the entry: ",tempDict)
        pickle.dump(tempDict, f)
        f.close()

    def viewAllBooks(self):
        f = open(BooksHelper.dbFileName,"rb")
        record = 0
        while 1:
            try:
                tempDict= pickle.load(f)
                for k,v in tempDict.items():
                    record = record+1
                    if record == 1:
                        print( '-'*75)
                        print ("%-10s %-25s %-25s %-15s" %("ISBN no", "Book Title", "Author Name", "location"))
                        print ('-'*75)
                    isbn_number, book_title, author_name, location = v
                    print ("%-10s %-25s %-25s %-15s" % (isbn_number, book_title, author_name, location))

            except EOFError:
                if record > 0:
                    print ('-'*75)
                else:
                    print ("No Record Found")
                    f.close()
                break
        input("Press any key to continue...")

        
    def deleteBookEntry(self, isbn_number):
        f= open(BooksHelper.dbFileName,"rb")
        while 1:
            try:
                tempDict =pickle.load(f)
                if isbn_number in tempDict.keys():
                    #if isbn number found delete entry
                    del tempDict[isbn_number]
                    f.close()
                    f= open(BooksHelper.dbFileName,"wb")
                    pickle.dump(tempDict,f)
                    f.close()
                    print( "Book with %s deleted successfully" %isbn_number)
                    break
            except EOFError:
                f.close()
                print ("Book not found")
                break
        input("Press any key to continue")


    def modifyBookEntrybyIsbn(self, isbn_no):
        f= open(BooksHelper.dbFileName,"rb")
        while 1:
            try:
                tempDict = pickle.load(f)
                if isbn_no in tempDict.keys():
                    isbn_number = input("Enter The ISBN number: ")
                    book_title = input("Enter Book Title: ")
                    author_name = input("Enter the Author Name: ")
                    location = input("Enter Location: ")
                    f.close()
                    self.addBook(isbn_number,book_title,author_name, location)
                    print ("Book with %s number modified successfully" %isbn_no)
                    break
            except EOFError:
                f.close()
                print ("Book with ISBN number %s not found" %isbn-no)
                break
        input("Press any key to continue")

    def searchBook(self, searchString):
        f= open(BooksHelper.dbFileName,"rb")
        record =0
        while 1:
            try:
                tempDict = pickle.load(f)
                for k,v in tempDict.items():
                    #["100","Book Name", "author", "Location"]
                    originalString = ' '.join(v).lower()
                    result = originalString.find(searchString.lower())
                    if result != -1:
                        record += 1
                        if record ==1:
                            print ('-'*75)
                            print ("%-10s %-25s %-25s %-15s" %("ISBN no", "Book Title", "Author Name", "location"))
                            print ('-'*75)

                        isbn_number,book_title,author_name, location =v
                        print ("%-10s %-25s %-25s %-15s" %(isbn_number,book_title,author_name, location))
            except EOFError:
                if record > 0:
                    print ('-'*75)
                    break
                else:
                    print( "Book not found")
                    f.close()
                    break
        input("Press any key to continue")
