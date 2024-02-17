class Library:
    def __init__(self):
        self.file = open("books.txt","a+")

    def list_books(self):
       self.file.seek(0)
       books = self.file.read().splitlines()
       if len(books) == 0 :
         print("The file is empty. Please add a book.")
       for book_inf in books :
           list = book_inf.strip().split(",")
           book_name = list[0]
           author = list[1]
           print(book_name , "," , author)
        

    def add_books(self):
       self.book_title = input("Book title:")
       self.book_author = input("Book author:")
       self.first_release_year = input("First release year:")
       self.number_of_pages = input("Number of pages:")
       str = self.book_title + "," + self.book_author + "," + self.first_release_year + "," + self.number_of_pages +"\n"
       self.file.write(str)

    def remove_book(self):
       delete =input("Which book do you want to delete? ")
       self.file.seek(0)
       books = self.file.read().splitlines()
       self.file.seek(0)
       self.file.truncate()

       for book_inf in books:
          list = book_inf.strip().split(",")
          if delete != list[0] :
             self.file.write(book_inf)
             self.file.write("\n")
         

    def __del__(self):
       self.file.close()



while True :
    lib = Library() 
    print("""    \n       ****MENU****
      1-) List Books
      2-) Add Book
      3-) Remove Book
      Enter 'q' for quit.""")

    option = input("Please enter your option :")
   
    if option == str(1) :
       lib.list_books()
      
    elif option == str(2):
       lib.add_books()
    
    elif option == str(3) :
       lib.remove_book()
    
    elif option == "q" :
       break
    
    else :
       print("The option you choose is not available in the menu. Please look at the menu again. ")

