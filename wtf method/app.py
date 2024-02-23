from flask import Flask, redirect, render_template, request, url_for
from forms import StudentForm

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] != 'dhana' or \
         request.form['password'] != 'dhana':
         error = 'Invalid username or password. Please try again!'
      else:
         return redirect(url_for('main'))
			
   return render_template('login.html', error = error)

students = []
@app.route('/main', methods=['GET', 'POST'])
def main():
    form = StudentForm()

    if form.validate_on_submit():
        student_data = {
            'name': form.name.data,
            'age': form.age.data,
            'grade': form.grade.data
        }
        students.append(student_data)

    return render_template('main.html', form=form, students=students)

if __name__ == "__main__":
   app.run(debug = True)