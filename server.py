from flask import Flask
from flask import render_template
from bot import bot

# Setting up server

app = Flask(__name__)

@app.route('/'+os.getenv('SECRET'))
def update():
    return "ok", 200

@app.route('/')
def server():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)