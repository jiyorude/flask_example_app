from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
    else:
        name = "World"

    if not name:
        name = "World"
    
    return render_template('greet.html', input_name=name)

@app.route('/clock')
def clock():
    return render_template('clock.html')

if __name__ == "__main__":
    app.run()
