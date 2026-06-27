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
    conn.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            resume_text TEXT,
            applied_date TEXT NOT NULL,
            FOREIGN KEY(job_id) REFERENCES jobs(id)
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

@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply(job_id):
    conn = get_db()
    job = conn.execute('SELECT * FROM jobs WHERE id = ?', (job_id,)).fetchone()

    if not job:
        conn.close()
        return "Job not found", 404

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        resume_text = request.form.get('resume_text', '').strip()

        if name and email:
            conn.execute('''
                INSERT INTO applications (job_id, name, email, phone, resume_text, applied_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (job_id, name, email, phone, resume_text, datetime.now().strftime('%Y-%m-%d %H:%M')))
            conn.commit()
            conn.close()
            return redirect('/')

    conn.close()
    return render_template('apply.html', job=job)

@app.route('/applications')
def applications():
    conn = get_db()
    rows = conn.execute('''
        SELECT applications.*, jobs.title AS job_title, jobs.company AS job_company
        FROM applications
        JOIN jobs ON jobs.id = applications.job_id
        ORDER BY applications.id DESC
    ''').fetchall()
    conn.close()
    return render_template('applications.html', applications=rows)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
