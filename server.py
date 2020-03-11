from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HellHiiiiiiiiiiiio, World!'


@app.route('/double_it/<int:namber>')
def multiply_by_two(namber):
    return str(namber*2)


#@app.route('/guess_the_number/<int:namber>')
#def guess (namber):
#    did_you_guess = 'no'
#    return ('did_you_guess: ' + did_you_guess)
#Guess The Number
#Write a programme where the computer randomly generates a number between 0 and 20. The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. This will get you started with the random library if you haven't already used it.



