class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.__price = price
        self.copies = copies

    def display(self):
        print(f"ISBN :{self.isbn}")
        print(f'Title : {self.title}')
        print(f"price :{self.__price}")
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

    @property
    def prices(self):
        return self.__price

    @prices.setter
    def prices(self, newPrice):
        if 50 > self.__price > 1000:
            self.__price = newPrice

        else:
            raise ValueError('Value Error Cannot be less than 50 and more than 1000')


book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 500, 10)
book2 = Book('989-1-16-589889-3', 'Learn Chemistry', 'Jack', 'CBC', 450, 1970, 16)
book3 = Book('966-1-16-1122349-3', 'Learn Chemistry', 'Jakir hosen', 'CBC', 950, 1070, 27)



book1.display()
book2.display()
book3.display()

book1.prices = 999 
