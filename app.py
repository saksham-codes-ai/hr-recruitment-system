from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''<!DOCTYPE html>
<html>
<head><title>HR System</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#667eea,#764ba2);color:white;text-align:center;padding:50px;}
h1{font-size:3em;}
.btn{background:white;color:#667eea;padding:15px 40px;text-decoration:none;border-radius:50px;font-weight:bold;}
</style>
</head>
<body>
<h1>HR Recruitment System</h1>
<p>AI-Powered Job Posting</p>
<a href="/create-job" class="btn">Create Job Posting</a>
</body>
</html>'''

@app.route('/create-job', methods=['GET', 'POST'])
def create_job():
    if request.method == 'POST':
        title = request.form.get('title', '')
        company = request.form.get('company', '')
        location = request.form.get('location', '')
        
        return f'''<!DOCTYPE html>
<html>
<head><title>Success</title>
<style>
body{font-family:Arial;background:linear-gradient(135deg,#667eea,#764ba2);color:white;text-align:center;padding:50px;}
h1{font-size:2.5em;}
.btn{background:white;color:#667eea;padding:15px 40px;text-decoration:none;border-radius:50px;font-weight:bold;margin:10px;}
</style>
</head>
<body>
<h1>✅ Job Posted!</h1>
<h2>{title}</h2>
<p>{company} - {location}</p>
<a href="/" class="btn">Home</a>
<a href="/create-job" class="btn">Post Another</a>
</body>
</html>'''
    
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
    app.run(host='0.0.0.0')
