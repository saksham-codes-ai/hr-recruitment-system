from flask import Flask, request, redirect, render_template
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
DATABASE = '/tmp/hr_system.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL,
            posted_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    conn = get_db()
    jobs = conn.execute('SELECT * FROM jobs ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', jobs=jobs)

@app.route('/create-job', methods=['GET', 'POST'])
def create_job():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        company = request.form.get('company', '').strip()
        location = request.form.get('location', '').strip()

        if title and company and location:
            conn = get_db()
            conn.execute(
                'INSERT INTO jobs (title, company, location, posted_date) VALUES (?, ?, ?, ?)',
                (title, company, location, datetime.now().strftime('%Y-%m-%d %H:%M'))
            )
            conn.commit()
            conn.close()
            return redirect('/')

    return render_template('create_job.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
