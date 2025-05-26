from flask import Flask, render_template, request
import models

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        course = request.form['course']
        info = [name,age,grade,course]
        return render_template('view_grades.html', info=info) #WE ADD INFO TO CLASS NOT TO RENDER!!!
    return render_template('add_student.html')

@app.route('/view_grades') #REFACTORING!!!
def view_grades():
    
    info = request.args.getlist('info') if request.args else []
    
    return render_template('view_grades.html', info=info)

if __name__ == '__main__':
    app.run()