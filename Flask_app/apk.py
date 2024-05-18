from flask import Flask, render_template, request, url_for, redirect
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': 'Vitm@0858',
    'host': 'localhost',
    'database': 'studentdb'
}

def calculate_percentage(marks):
    total_marks = sum(marks)
    percentage = (total_marks / (len(marks) * 100)) * 100
    return percentage

def setup_database():
    conn = mysql.connector.connect(
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host']
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS studentdb")
    cursor.execute("USE studentdb")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS school_pcm (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            Physics INT NOT NULL,
            Maths INT NOT NULL,
            Chemistry INT NOT NULL,
            English INT NOT NULL,
            Hindi INT NOT NULL,
            Percentage FLOAT NOT NULL,
            Result VARCHAR(10) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/result', methods=['POST'])
def result():
    marks = []
    for subject in ['Physics', 'Maths', 'Chemistry', 'English', 'Hindi']:
        marks.append(int(request.form[subject]))
    percentage = calculate_percentage(marks)
    name = request.form['Name']
    result_message = 'Pass' if percentage >= 50 else 'Fail'
    return render_template('result.html', name=name, percentage=percentage, result=result_message)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['Name']
    Physics = int(request.form['Physics'])
    Maths = int(request.form['Maths'])
    Chemistry = int(request.form['Chemistry'])
    English = int(request.form['English'])
    Hindi = int(request.form['Hindi'])
    
    marks = [Physics, Maths, Chemistry, English, Hindi]
    percentage = calculate_percentage(marks)
    result_message = 'Pass' if percentage >= 50 else 'Fail'

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO school_pcm (name, Physics, Maths, Chemistry, English, Hindi, Percentage, Result)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (name, Physics, Maths, Chemistry, English, Hindi, percentage, result_message))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

@app.route('/source/')
def source():
    return render_template('table.html')

if __name__ == '__main__':
    setup_database()
    app.run(debug=True, port=912)
