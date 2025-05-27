from flask import Flask, render_template, request
import models

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student(): #REFACTORING
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        course = request.form['course']

        info = models.Student(name, age, {})
        info.add_grade(self, course, grade)

        return render_template('view_grades.html') #WE ADD INFO TO CLASS NOT TO RENDER!!!
    return render_template('add_student.html')

@app.route('/view_grades', methods=['GET', 'POST']) #REFACTORING!!!
def view_grades():
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    course = request.form['course']

    info = models.Student(name, age, {})

    return render_template('view_grades.html', name=name, course=course, grade=grade, students={'kek', 'lol'}, student=info)

if __name__ == '__main__':
    app.run()