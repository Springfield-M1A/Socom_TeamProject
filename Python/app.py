from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('HTML/index.html')

@app.route('/stock')
def stock():
    return render_template('HTML/stock.html')

@app.route('/prediction')
def prediction():
    return render_template('HTML/prediction.html')

@app.route('/beginner')
def beginner():
    return render_template('HTML/beginner.html')

if __name__ == '__main__':
    app.run()
