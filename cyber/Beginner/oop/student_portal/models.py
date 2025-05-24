'''
TO-DO
Replace data to __init__ as shared value
Fix replace 
Fix get_student_drade method
'''

class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = dict(grades)

    data = dict()

    def add_grade(self, course, grade):
        self.data[course] = grade

    def get_grades(self):
        for course in self.data:
            print(course, self.data[course])

class Course:
    def __init__(self, name_course, list_students):
        self.name_couse = name_course
        self.list_students = list_students

    data = dict()

    def add_student(self, student):
        self.data['name_student'] = student

    def get_student_grades(self, student_name):
        for i in self.list_students:
            if i == student_name:
                print(grade,'w')

alex = Student('Alex', 19, {})
alex.add_grade('Math', 3)
alex.add_grade('Bialoge', 2)
alex.get_grades()

math = Course('Math', {})
math.add_student('Alex')
math.add_student('Felix')
math.get_student_grades(alex.name)