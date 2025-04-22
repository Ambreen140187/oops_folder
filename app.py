from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 🧠 OOP Class for Student
class Student:
    def __init__(self, roll_no, name, grade):
        self.roll_no = roll_no
        self.name = name
        self.grade = grade

students = []  # Temporary storage (no DB used)

# 🌐 Home Page
@app.route('/')
def index():
    return render_template('index.html', students=students)

# ➕ Add Student
@app.route('/add', methods=['POST'])
def add_student():
    roll_no = request.form['roll_no']
    name = request.form['name']
    grade = request.form['grade']
    new_student = Student(roll_no, name, grade)
    students.append(new_student)
    return redirect('/')

# ✏️ Edit Student
@app.route('/edit/<roll_no>')
def edit_student(roll_no):
    for student in students:
        if student.roll_no == roll_no:
            return render_template('edit.html', student=student)
    return redirect('/')

# 🔄 Update Student
@app.route('/update/<roll_no>', methods=['POST'])
def update_student(roll_no):
    for student in students:
        if student.roll_no == roll_no:
            student.name = request.form['name']
            student.grade = request.form['grade']
            break
    return redirect('/')

# ❌ Delete Student
@app.route('/delete/<roll_no>')
def delete_student(roll_no):
    global students
    students = [student for student in students if student.roll_no != roll_no]
    return redirect('/')

# 🚀 Run Server
if __name__ == '__main__':
    app.run(debug=True)
