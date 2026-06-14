from flask import Flask, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>HR Recruitment System</title>
    <style>
        body { 
            font-family: Arial; 
            background: linear-gradient(135deg, #667eea, #764ba2); 
            color: white; 
            text-align: center; 
            padding: 50px; 
            margin: 0;
        }
        h1 { font-size: 3em; margin-bottom: 20px; }
        p { font-size: 1.3em; margin-bottom: 40px; }
        .btn { 
            background: white; 
            color: #667eea; 
            padding: 15px 40px; 
            text-decoration: none; 
            border-radius: 50px; 
            font-weight: bold;
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <h1>HR Recruitment System</h1>
    <p>AI-Powered Job Posting & Interview Management</p>
    <a href="/create-job" class="btn">Create Job Posting</a>
</body>
</html>'''

# Create Job Posting page
@app.route('/create-job', methods=['GET', 'POST'])
def create_job():
    if request.method == 'POST':
        try:
            title = request.form.get('title', '')
            company = request.form.get('company', '')
            location = request.form.get('location', '')
            description = request.form.get('description', '')
            requirements = request.form.get('requirements', '')
            salary = request.form.get('salary', '')
            
            # Job posted! Show success message
            return f'''<!DOCTYPE html>
<html>
<head>
    <title>Job Posted!</title>
    <style>
        body { 
            font-family: Arial; 
            background: linear-gradient(135deg, #667eea, #764ba2); 
            color: white; 
            text-align: center; 
            padding: 50px; 
        }
        h1 { font-size: 2.5em; }
        .success { background: rgba(255,255,255,0.2); padding: 30px; margin: 20px; border-radius: 15px; }
        .btn { 
            background: white; 
            color: #667eea; 
            padding: 15px 40px; 
            text-decoration: none; 
            border-radius: 50px; 
            font-weight: bold;
            display: inline-block;
            margin: 10px;
        }
    </style>
</head>
<body>
    <h1>✅ Job Posted Successfully!</h1>
    <div class="success">
        <h2>{title}</h2>
        <p><strong>Company:</strong> {company}</p>
        <p><strong>Location:</strong> {location}</p>
        <p><strong>Description:</strong> {description}</p>
        <p><strong>Requirements:</strong> {requirements}</p>
        <p><strong>Salary:</strong> {salary}</p>
    </div>
    <a href="/" class="btn">Home</a>
    <a href="/create-job" class="btn">Post Another Job</a>
</body>
</html>'''
        except Exception as e:
            return f'''<h1>Error: {str(e)}</h1><a href="/create-job">Try Again</a>'''
    
    # Show form (GET request)
    return '''<!DOCTYPE html>
<html>
<head>
    <title>Create Job Posting</title>
    <style>
        body { 
            font-family: Arial; 
            background: linear-gradient(135deg, #667eea, #764ba2); 
            color: white; 
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            background: rgba(255,255,255,0.1);
            padding: 40px;
            border-radius: 15px;
        }
        h1 { text-align: center; font-size: 2.5em; margin-bottom: 30px; }
        input, textarea {
            width: 100%;
            padding: 15px;
            margin: 10px 0;
            border: none;
            border-radius: 10px;
            background: white;
            color: #333;
            font-size: 1em;
        }
        textarea { height: 150px; }
        button {
            width: 100%;
            padding: 15px;
            background: white;
            color: #667eea;
            border: none;
            border-radius: 50px;
            font-size: 1.2em;
            font-weight: bold;
            margin-top: 20px;
            cursor: pointer;
        }
        .back { text-align: center; margin-top: 20px; }
        .back a { color: white; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 Create Job Posting</h1>
        <form method="POST">
            <input type="text" name="title" placeholder="Job Title" required>
            <input type="text" name="company" placeholder="Company Name" required>
            <input type="text" name="location" placeholder="Location" required>
            <textarea name="description" placeholder="Job Description"></textarea>
            <textarea name="requirements" placeholder="Requirements"></textarea>
            <input type="text" name="salary" placeholder="Salary Range">
            <button type="submit">Post Job</button>
        </form>
        <div class="back">
            <a href="/">← Back to Home</a>
        </div>
    </div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
