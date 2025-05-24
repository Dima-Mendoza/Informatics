class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sound(self):
        print('Unknown animal')

class Dog(Animal):
    def sound(self):
        print('Gav Gav!')

class Cat(Animal):
    def sound(self):
        print('Meow Meow')

bird = Animal('Gosha', 5)
cat = Cat('Xeon', 5)
dog = Dog('Rover', 5)

bird.sound()
cat.sound()
dog.sound()

print('\n\n')

''' END FIRST TASK'''

class Vehicle:
    def move(self):
        print('Vehicle is moving')

class Car(Vehicle):
    def move(self):
        print('Car is moving on road')

class Bike(Vehicle):
    def move(self):
        print('Bike is MOVING!!!')

class Boat(Vehicle):
    def move(self):
        print('Boat is watering on ocean')

def move_vehicle(vehicle):
    vehicle.move()

tank_t90 = Vehicle()
porshe = Car()
bmx = Bike()
yacht = Boat()

move_vehicle(tank_t90)
move_vehicle(porshe)
move_vehicle(bmx)
move_vehicle(yacht)

print('\n\n')

'''END SECOND TASK'''

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = list(grades)

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        avg_grade = 0
        for i in self.grades:
            avg_grade += i
        return avg_grade/len(self.grades)

student1 = Student('Alexa', 19,[])
student2 = Student('Felix', 20,[])

student1.add_grade(4)
student1.add_grade(3)
student2.add_grade(5)

with open('student_data.txt', 'w') as file:
    file.write(f"Name: {student1.name}, Age: {student1.age}, avg_gr: {student1.average_grade()}\n")
    file.write(f"Name: {student2.name}, Age: {student2.age}, avg_gr: {student2.average_grade()}\n")


'''END THIRD TASK'''

class Book:
    def __init__(self, author, title, year):
        self.title = title
        self.author = author
        self.year = year

class Library:

    data = list()

    def add_book(self, book):
        self.data.append(book)

    def remove_book(self, title):
        for i in range(len(self.data)):
            if str(self.data[i].title) == title:
                self.data.pop(i)
                break

    def find_books_by_author(self, author):
        for i in range(len(self.data)):
            if str(self.data[i].author) == author:
                print(f'Author {self.data[i].author} {self.data[i].title} {self.data[i].year}')
    
    def list_books(self):
        for i in range(len(self.data)):
            print(f'List {self.data[i].author} {self.data[i].title} {self.data[i].year}')

library = Library()

book1 = Book('Kek', 'Lolita', 1984)
book2 = Book('Kak', 'Angles', 1999)
book3 = Book('Kak', 'How?', 2001)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.remove_book('Lolita')
library.list_books()
library.find_books_by_author('Kak')