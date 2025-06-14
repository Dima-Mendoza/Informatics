from flask import Flask, render_template, request, url_for, redirect
from models import Student, Course

app = Flask(__name__)

#DATA BASE
students = {}
courses = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        course_name = request.form['course']

        students[name] = Student(name,age) #AI add
        student = students[name]
        courses[course_name] = Course(course_name)
        course = courses[course_name]

        course.add_student(student)
        student.add_grade(course_name,grade)

        return redirect(url_for('view_grades'))#END AI ADD
    return render_template('add_student.html')

@app.route('/view_grades')
def view_grades():
    return render_template('view_grades.html', students=students)

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():#REFACTORING PART 2.1
    if request.method == 'POST':
        course_name = request.form['course_name']
        max_students = request.form['max_students']

        courses[course_name] = Course(course_name)
        courses[course_name + '_max'] = max_students
        return redirect(f'/course/{course_name}')

    return render_template('add_course.html')

@app.route('/course/<course_name>')
def course_info(course_name):
    course = Course(course_name)
    #course.get_student_grades()

    if not course:
        abort(404, description="Not found")
    else:
        return render_template('course.html', 
        course_name=course_name, average_grade=students, students=students)

@app.route('/student/<student_name>')
def student_info():
    pass


if __name__ == '__main__':
    app.run()