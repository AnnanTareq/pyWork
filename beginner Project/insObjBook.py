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
book3 = Book('878-2-11-434322-4','Learn Molecular Chemistry', 'Jack', 'CBC',50, 170, 50)
book4 = Book('534-3-54-736422-2','Learn Physics', 'Stuart', 'CBC',20, 100, 22)


books = [book1, book2, book3, book4]

# for i in range(len(books)):
#     books[i].display()
#

for book in books:
    book.display()

jacks_book = [book1.title for book1 in books if book1.author == 'Jack']
print(jacks_book)

