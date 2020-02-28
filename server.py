from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HellHiiiiiiiiiiiio, World!'


@app.route('/double_it/<int:namber>')
def multiply_by_two(namber):
    return str(namber*2)

