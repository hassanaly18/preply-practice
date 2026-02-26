class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            print("You borrowed ", self.title, "from our library")
            self.available = False
        else:
            print("Book is not available")  
            
    def return_book(self):
        if self.available:
            print("Book is already in the library, Cant return")
        else: 
            print("Thanks for returning the book")
            self.available = True 
    
    def show_status(self):
        print("Title:", self.title, "\nAuthor:", self.author, "\nAvailable:", self.available)                     
                