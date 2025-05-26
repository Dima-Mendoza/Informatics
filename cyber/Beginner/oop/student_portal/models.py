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
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_grades(self):
        for course in self.grades:
            print(course, self.grades[course])

class Course:
    def __init__(self, name_course, list_students):
        self.name_couse = name_course
        self.list_students = {}

    def add_student(self, student):
        self.list_students[student] = self.name_couse

    def get_student_grades(self, student_name):
        print(self.list_students.items())
        for i in self.list_students:
            if i == student_name.name:
                print(student_name.grades[self.name_couse])

# alex = Student('Alex', 19, {})
# alex.add_grade('Math', 3)
# alex.add_grade('Bialoge', 2)
# alex.get_grades()

# math = Course('Math', {})
# math.add_student('Alex')
# math.add_student("Felix")
# math.get_student_grades(alex)