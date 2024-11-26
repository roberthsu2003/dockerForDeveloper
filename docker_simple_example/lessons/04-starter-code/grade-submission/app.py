from flask import Flask, render_template, request, redirect, url_for
from grade import Grade
import constants

app = Flask(__name__)
student_grades = []

def get_grade_index(id):
    for i, grade in enumerate(student_grades):
        if grade.id == id:
            return i
    return constants.NOT_FOUND

@app.route('/', methods=['GET'])
def get_form():
    print("inside of get form")
    id = request.args.get('id')
    index = get_grade_index(id)
    grade = Grade() if index == constants.NOT_FOUND else student_grades[index]
    return render_template('form.html', grade=grade)

@app.route('/handleSubmit', methods=['POST'])
def submit_form():
    form_data = request.form
    grade = Grade(name=form_data['name'], subject=form_data['subject'], score=form_data['score'], id=form_data['id'])
    index = get_grade_index(grade.id)
    if index == constants.NOT_FOUND:
        student_grades.append(grade)
    else:
        student_grades[index] = grade
    return redirect(url_for('get_grades'))

@app.route('/grades', methods=['GET'])
def get_grades():
    return render_template('grades.html', grades=student_grades)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')