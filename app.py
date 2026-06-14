from flask import Flask

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
