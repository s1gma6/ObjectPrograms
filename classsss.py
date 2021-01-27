#Simple Object Oriented Programming Implementation

#Shivaram Kumar National Public School Jayanagar
#Assignment: Implementation of Inheriatnce in Python using OOP

#Accessing different variables between two classes
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Topic:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def classnames(self):
        for i in self.students:
            return(i)

    def avg_grade(self):
        value = 0
        for i in self.students:
            value += i.get_grade()
        return value / len(self.students)
 
#Inheritance examples
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def speak(self):
        super().__init__(name, age) #Make sure to remember this, it references the parent class
        return "Meow"
    
class Dog(Pet):
    def speak(self):
        super().__init__(name, age) #Make sure to remember this, it references the parent class
        return "Bonk"

#Class Attributes and Class methods
class Person: 
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.addperson()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people()

    @classmethod
    def addperson(cls):
        cls.number_of_people += 1

#Static Methods
class Math:
    
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(y):
        return y + 10





