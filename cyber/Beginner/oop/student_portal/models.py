class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_grades(self):
        for course in self.grades:
            return self.grades[course]
    
    def get_average_grade(self):
        avg = 0
        for i in self.grades.values():
            avg += i
        return avg / int(len(self.grades))


class Course:
    def __init__(self, name_course):
        self.name_couse = name_course
        self.list_students = {}

    def add_student(self, student):
        self.list_students[student] = self.name_couse

    def get_student_grades(self, student_name):
        #print(self.list_students.items())
        for i in self.list_students:
            if i == student_name.name:
                return student_name.grades[self.name_couse]
    
    def get_top_students(self, n):
        return list(self.list_students).sort()[:5]

    def remove_student(self, student_name):
        for i in self.list_students:
            if i == student_name.name:
                student_name.pop(i)

# alex = Student('Alex', 19, {})
# alex.add_grade('Math', 3)
# alex.add_grade('Bialoge', 2)
# alex.get_grades()

# math = Course('Math', {})
# math.add_student('Alex')
# math.add_student("Felix")
# math.get_student_grades(alex)