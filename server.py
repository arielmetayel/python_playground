import random
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
#Write a programme where the computer randomly 
# generates a number between 0 and 20. The user needs to guess what the number is. 
# If the user guesses wrong, tell them their guess is either too high, or too low. 
# This will get you started with the random library if you haven't already used it.




def guess_the_number():
#function prints a flow of guessing a number and prnting if it is less/more/same as a random number.
    gussed_number = int(input("guess a number between 1 and 20:  "))
    compare_to_this = random.randint(1,20)
    if (gussed_number == compare_to_this):
        print ('yay')
    elif (gussed_number > compare_to_this):
        print ('you guessed too high')
    else:  
        print ('you guessed too low')
    return     

#guess_the_number ()
