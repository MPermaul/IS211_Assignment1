class Book:
    """This is a class tthat represents a book. 
      
    Attributes: 
        author (string): Author of the book. 
        title (string): The title of the book. 
    """

    def __init__ (self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print('\'{}\' written by {}'.format(self.title,self.author))


book1 = Book('John Steinbeck','Of Mice and Men')
book2 = Book('Harper Lee', 'To Kill a Mockingbird')

book1.display()
book2.display()
