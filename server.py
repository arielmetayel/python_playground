import random
import time
import matplotlib.pyplot as plt
import numpy as np


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

def playing_with_numpy():
    a = np.array([(0,1,2,3,4,5),(6,7,8,9,10,11)])
    print(a)
    print(a.ndim)
    print(a.size)
    print(a.shape)
    print(np.sum(a))
    return()






def plotting_sin_cos ():
    welcome_message('plotting_sin_cos')

    x = np.linspace(-10, 10, 100)
    print (x)
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.show()
    return ()




def welcome_message(function_name):
    print ('Loading your game...')
    for line in range (1,8):
        for x in range (1,8):
            print(":)" * x, end = '\r')
            time.sleep(0.1)
        print("                         ", end = '\r')
    print ('\n\n\nwelcome to the --',function_name, '-- game!\n \n \n')
    time.sleep(2)
    return()


def rock_paper_scissors ():
#Make a rock-paper-scissors game where it is the player 
# vs the computer. The computer’s answer will be randomly 
# generated, while the program will ask the user for their input. 
    welcome_message('rock_paper_scissors')

    selection = ['r','p','s']
    score = {'player':0, 'computer':0}

    #welcoming the user
    print ('\n let\'s play! \n try to win against the computer in rock, paper, scissors\n \n \
    first one who reaches 3 is the winner! \n \n \
    r for rock, p for paper, s for scissors:')
    time.sleep(2)
    
    while (score['player'] < 3) and (score['computer'] < 3):
    #get the input
        user_rps = input ('Your turn (r/p/s):')
        while user_rps not in selection:
            user_rps = input ('wrong input. try only (r/p/s):') 
    #check for the winner of the mini game
        computer_rps = random.choice(selection)
        print ('computer went with: ', computer_rps, end = ' - ')
        if computer_rps == user_rps:
            print ('it\'s a tie')
        elif computer_rps == "r":
            if user_rps == "s":
                score['computer'] += 1
                print('computer wins')
            else:
                score['player'] += 1
                print('you win')
        elif computer_rps == "p":
            if user_rps == "r":
                score['computer'] += 1
                print('computer wins')
            else:
                score['player'] += 1
                print('you win')
        elif computer_rps == "s":
            if user_rps == "p":
                score['computer'] += 1
                print('computer wins')
            else:
                score['player'] += 1
                print('you win')

    #print the result
    print ('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- \n and the final score is... \n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
    
    for each in score:
        print (each,'-->',score[each])
    print ('-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

    return ()


def guess_the_number():
#function prints a flow of guessing a number and prnting if it is less/more/same as a random number.
    welcome_message('guess_the_number')

    gussed_number = int(input("guess a number between 1 and 20:  "))
    compare_to_this = random.randint(1,20)
    if (gussed_number == compare_to_this):
        print ('yay')
    elif (gussed_number > compare_to_this):
        print ('you guessed too high')
    else:  
        print ('you guessed too low')
    return     

#For this project, you will have a generate a sine vs cosine curve. 
# You will need to use the numpy library to access the sine and cosine 
# functions. You will also need to use the matplotlib library to draw the curve. 
# To make this more difficult, make the graph go from -360° to 360°, with there 
# being a 180° difference between each point on the x-axis.


#guess_the_number ()
#rock_paper_scissors()
#welcome_message('Nurrrrrr')
#plotting_sin_cos ()
#playing_with_numpy ()