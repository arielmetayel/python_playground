import random
import time
import matplotlib.pyplot as plt
import numpy as np
import string

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


def playing_with_numpy():
    a = np.array([     (0,1,2,3,4,5), (6,7,8,9,10,11), (6,7,8,9,10,11)])
    print(a)
    print(a.ndim)
    print(a.size)
    print(a.shape)
    print(np.sum(a))
    return()



def hangman ():
#This is probably the hardest one out of these 6 small projects. 
# This will be similar to guessing the number, except we are guessing 
# the word. The user needs to guess letters,Give the user no more 
# than 6 attempts for guessing wrong letter. This will mean you will 
# have to have a counter. You can download a ‘sowpods’ dictionary 
# file or csv file to use as a way to get a random word to use.

#get a word. break it to letters
#accepts input
#if input is within the letters, show them. otherwise show _ _ _ _ _ 
#variables: total attempts up to 6

    welcome_message('hangman')

    bag_of_words = ['chillie', 'pepper']
    selected_word = random.choice(bag_of_words)
    letters_for_guessing = list(selected_word)
    wrong_attempts = 6
    
    #adding counter for each letter, removing the first empty variable
    letters_with_index = [[]]
    for letter in letters_for_guessing:
        letters_with_index.append([letter,0])
    letters_with_index.pop(0)

    sum = 0

    while (sum < len(letters_with_index) and (wrong_attempts>0)):
        guess = input("guess a letter: ")
        found = False
        for i in range(0,len(letters_with_index)):
            if guess == letters_with_index[i][0]:
                if letters_with_index[i][1] == 0:
                    found = True
                letters_with_index[i][1] = 1
        if not found:
            wrong_attempts -=1
        
        #check if the word is completely guessed
        print(wrong_attempts, 'more tries. so far you guessed: ')
        sum = 0
        for j in range(0,len(letters_with_index)):
            sum += letters_with_index[j][1]
            if letters_with_index[j][1] == 0:
                print ('_',end = " ")
            else:
                print (letters_with_index[j][0], end = " ")
        print("")
    if sum == len(letters_with_index):
        print ('you won! come back house is suuposed to win')
    else:
        print ('you got hanged! bye bye')
    return()
    


def password_generator():
#Write a programme, which generates a 
# random password for the user. Ask the user how 
# long they want their password to be, and how many letters 
# and numbers they want in their password. Have a mix of upper and 
# lowercase letters, as well as numbers and symbols. The password 
# should be a minimum of 6 characters long.
    welcome_message('password_generator')
    possibilities = list(string.printable)
    
    password_length = int(input('how long of a password would you need? (choose a number between 6 - 14:  '))
    while ((password_length>14) or (password_length<6)):
        password_length = int(input('we need this to be number between 6 - 14:  '))    

    password = []
    password = random.choices(possibilities,k = password_length)
    print(password)
    printable_password = "".join(password)
    print ('Here is your new shiny password (',password_length,'chars):',printable_password)



def plotting_sin_cos ():
    welcome_message('plotting_sin_cos')

    x = np.linspace(-10, 10, 100)
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.show()
    return ()





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
#password_generator ()
hangman()
