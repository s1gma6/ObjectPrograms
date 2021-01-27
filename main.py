
class Person():
    def __init__(self, name, age, height, topic):
        self.name = name
        self.age = age
        self.height = height
        self.topic = topic

    def get_name(self):
        return self.name

class Tanvi(Person):

    def __init__(self, books, char, name, age, height, topic):
        self.books = books
        self.char = char

    def get_books(self):
        print(self.name, "likes to read", self.books)

    def get_char(self):
        print(self.name, "is intereseted in", self.char)


p1 = Tanvi("LOTR", "Aragorn", "Tanvi", 16, 174, "CSE")

print(p1.get_char())
