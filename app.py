from flask import Flask, request, redirect
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# Database configuration
DATABASE = 'hr_system.db'

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database with jobs table"""
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
    print("✅ Database initialized!")

# Initialize database on start
init_db()

@app.route('/')
def home():
    conn = get_db()
    jobs = conn.execute('SELECT * FROM jobs ORDER BY posted_date DESC').fetchall()
    conn.close()
    
    jobs_html = ''
    for job in jobs:
        jobs_html += f'''
        <div class="job-card">
            <h3>{job['title']}</h3>
            <p><strong>{job['company']}</strong> - {job['location']}</p>
            <p>Posted: {job['posted_date']}</p>
            <a href="/apply/{job['id']}" class="btn-small">Apply Now</a>
        </div>
        '''
    
    if not jobs_html:
        jobs_html = '<p class="no-jobs">No jobs posted yet. Create one!</p>'
    
    return f'''<!DOCTYPE html>
<html>
<head><title>HR System</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#667eea,#764ba2);color:white;text-align:center;padding:50px;}
h1{font-size:3em;}
.btn{background:white;color:#667eea;padding:15px 40px;text-decoration:none;border-radius:50px;font-weight:bold;}
.jobs-section{margin:50px auto;}
.jobs-section h2{font-size:2em;margin-bottom:30px;}
.job-card{background:rgba(255,255,255,0.15);padding:20px;margin:15px auto;border-radius:10px;max-width:600px;text-align:left;}
.job-card h3{font-size:1.5em;margin-bottom:10px;}
.job-card p{margin:5px 0;}
.btn-small{background:white;color:#667eea;padding:10px 25px;text-decoration:none;border-radius:5px;display:inline-block;margin-top:10px;font-weight:bold;}
.no-jobs{font-size:1.2em;opacity:0.8;}
</style>
</head>
<body>
<h1>🏢 HR Recruitment System</h1>
<p>AI-Powered Job Posting & Interview Management</p>
<a href="/create-job" class="btn">Create Job Posting</a>

<div class="jobs-section">
<h2>📋 Available Jobs</h2>
{jobs_html}
</div>
</body>
</html>'''

@app.route('/create-job', methods=['GET', 'POST'])
def create_job():
    if request.method == 'POST':
        title = request.form.get('title', '')
        company = request.form.get('company', '')
        location = request.form.get('location', '')
        
        # Save to database
        conn = get_db()
        conn.execute(
            'INSERT INTO jobs (title, company, location, posted_date) VALUES (?, ?, ?, ?)',
            (title, company, location, datetime.now().strftime('%Y-%m-%d %H:%M'))
        )
        conn.commit()
        conn.close()
        
        return redirect('/')
    
    return '''<!DOCTYPE html>
<html>
<head><title>Create Job</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#667eea,#764ba2);color:white;margin:0;padding:20px;}
.container{max-width:500px;margin:50px auto;background:rgba(255,255,255,0.1);padding:40px;border-radius:15px;}
input{width:100%;padding:15px;margin:10px 0;border:none;border-radius:10px;background:white;color:#333;}
button{width:100%;padding:15px;background:white;color:#667eea;border:none;border-radius:50px;font-weight:bold;margin-top:20px;}
.back{text-align:center;margin-top:20px;}
.back a{color:white;}
</style>
</head>
<body>
<div class="container">
<h1>📝 Create Job</h1>
<form method="POST">
<input type="text" name="title" placeholder="Job Title" required>
<input type="text" name="company" placeholder="Company" required>
<input type="text" name="location" placeholder="Location" required>
<button type="submit">Post Job</button>
</form>
<div class="back"><a href="/">← Back</a></div>
</div>
</body>
</html>'''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
