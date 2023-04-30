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
        print('*' * 50)

    def in_stock(self):
        if self.copies > 0:
            return True
        else:
            return False

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print('Out of stock')


book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 500, 10)
book2 = Book('989-1-16-589889-3', 'Learn Chemistry', 'Jack', 'CBC', 450, 970, 16)
book3 = Book('966-1-16-1122349-3', 'Learn Chemistry', 'Jakir hosen', 'CBC', 950, 1070, 0)


book1.display()
# book2.display()
book3.display()

book1.in_stock()
book1.sell()
book1.display()

book3.in_stock()
