from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
import uuid
import time

app = Flask(__name__)

# Database configuration using environment variables
db_config = {
    'host': os.getenv('DATABASE_HOST', 'default_host'),
    'user': os.getenv('DATABASE_USER', 'default_user'),
    'password': os.getenv('DATABASE_PASSWORD', 'default_password'),
    'database': os.getenv('DATABASE_NAME', 'default_db')
}

def create_grades_table(retries=5, delay=5):
    for _ in range(retries):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS grades (
                    id VARCHAR(255) PRIMARY KEY,
                    name VARCHAR(255),
                    subject VARCHAR(255),
                    score VARCHAR(10)
                )
            ''')
            conn.commit()
            cursor.close()
            conn.close()
            print("Database initialized successfully")
            break
        except mysql.connector.Error as err:
            print("Database connection failed. Retrying...")
            time.sleep(delay)
    else:
        print("Failed to connect to the database after several attempts.")

create_grades_table()

# Grade Class
class Grade:
    def __init__(self, name=None, subject=None, score=None, id=None):
        self.name = name
        self.subject = subject
        self.score = score
        self.id = id

    def save_to_db(self):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Check if the grade already exists
        cursor.execute("SELECT COUNT(*) FROM grades WHERE id = %s", (self.id,))
        exists = cursor.fetchone()[0] > 0

        if exists:
            # Update existing record
            cursor.execute("UPDATE grades SET name=%s, subject=%s, score=%s WHERE id=%s",
                           (self.name, self.subject, self.score, self.id))
        else:
            # Insert new record
            self.id = str(uuid.uuid4())  # Generate new id for new record
            cursor.execute("INSERT INTO grades (id, name, subject, score) VALUES (%s, %s, %s, %s)",
                           (self.id, self.name, self.subject, self.score))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all_grades():
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, subject, score FROM grades")
        grades = [Grade(id=row[0], name=row[1], subject=row[2], score=row[3]) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return grades

    @staticmethod
    def get_grade_by_id(gid):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, subject, score FROM grades WHERE id = %s", (gid,))
        row = cursor.fetchone()
        grade = Grade(id=row[0], name=row[1], subject=row[2], score=row[3]) if row else None
        cursor.close()
        conn.close()
        return grade

@app.route('/', methods=['GET'])
def get_form():
    id = request.args.get('id')
    grade = Grade.get_grade_by_id(id) if id else Grade()
    return render_template('form.html', grade=grade)

@app.route('/handleSubmit', methods=['POST'])
def submit_form():
    form_data = request.form
    grade_id = form_data.get('id')  # Use get method to handle the case when 'id' is not in form_data
    grade = Grade(name=form_data['name'], subject=form_data['subject'], score=form_data['score'], id=grade_id)
    grade.save_to_db()
    return redirect(url_for('get_grades'))

@app.route('/grades', methods=['GET'])
def get_grades():
    grades = Grade.get_all_grades()
    return render_template('grades.html', grades=grades)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
