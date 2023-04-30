class Course:
    def __init__(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self.avg_rating = 0

    def __str__(self):
        return f'{self.title} by {self.instructor}'

    def new_user_enrolled(self, new):
        self.users.append(new)

    def received_a_rating(self, new_ratings):
        self.avg_rating = (self.avg_rating * self.ratings + new_ratings)/ (self.ratings + 1)
        self.ratings += 1

    def show_details(self):
        print(self.title)
        print(self.instructor)
        print(self.price)
        print(self.lectures)
        print(self.users)
        print(self.avg_rating)


class VideoCourse(Course):
    def __init__(self, title, instructor, lectures, price, length_video):
        super().__init__(title, instructor, lectures, price)
        self.length_video = length_video

    def show_details(self):
        super().show_details()
        print(self.length_video)

class pdf_Course(Course):
    def __init__(self, title, instructor, lectures, price, pages):
        super().__init__(title, instructor, lectures, price)
        self.pages = pages

    def show_details(self):
        super().show_details()
        print(self.pages)


vc = VideoCourse('Learn C++', 'Jack', 30, 50, 10)
vc.new_user_enrolled('Allen')
vc.new_user_enrolled('Max')
vc.new_user_enrolled('Tom')

vc.received_a_rating(3)
vc.received_a_rating(4)
vc.received_a_rating(5)

vc.show_details()