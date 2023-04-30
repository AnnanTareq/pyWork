class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print(f"ISBN :{self.isbn}")
        print(f'Title : {self.title}')
        print(f"price :{self.price}")
        print(f"Copies : {self.copies}")
        print('*'*50)


book1 = Book('957-4-36-547417-1','Learn Physics', 'Stephen', 'CBC',350, 500, 10)
book2 = Book('989-1-16-589889-3','Learn Chemistry', 'Jack', 'CBC',450, 970, 16)

book1.display()
book2.display()