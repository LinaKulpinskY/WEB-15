from flask import Flask, request, render_template, redirect, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FSFAFDSA'
app.config['UPLOAD_FOLDER'] = 'materials'


@app.route('/')
def index():
    return render_template('mars.html')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')