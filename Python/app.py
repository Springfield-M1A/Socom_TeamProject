from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('HTML/index.html')

@app.route('/')
def stock():
    return render_template('HTML/stock.html')

@app.route('/')
def prediction():
    return render_template('HTML/prediction.html')

@app.route('/')
def beginner():
    return render_template('HTML/beginner.html')

@app.route('/install_requirements', methods=['POST'])
def install_requirements():
    try:
        result = subprocess.run(["pip", "install", "-r", "requirements.txt"], capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({'message': 'Requirements 설치가 완료되었습니다.'})
        else:
            return jsonify({'message': 'Requirements 설치 중 오류가 발생하였습니다.'})
    except Exception as e:
        return jsonify({'message': 'Requirements 설치 중 오류가 발생하였습니다.'})

if __name__ == '__main__':
    app.run()