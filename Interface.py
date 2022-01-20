################# IMPORTING ALL LIBRARIES #################
import sys
import random
import os
import time

################# IMPORTING ALL LOCAL MODULES #################
import Quiz
import HigherOrLower
import Hangman

################# END OF IMPORTING #################

########################################### START OF INTERFACE #####################################################################

os.system('cls')        # Clears terminal
player = input("\nHello Player!\nEnter your name!\n>> ")

################# ADDING NAME TO A TEXT FILE #################
f = open('Scores.txt', 'a+')
f.write("\n")
f.write("-"*20)
f.write(f"\nPlayer: {player}")
f.close()
################# END OF ADDING NAME TO A TEXT FILE #################

while (True):

    os.system('cls')        # Clears terminal

    # Adapted from https://stackoverflow.com/questions/8907236/center-aligning-text-on-console-in-python
    # Some sort of graphics in the terminal
    print("{:^50}\n{:^50}\n{:^50}\n".format('-'*20, f"Hello {player.capitalize()}!", '-'*20))
    print("{:^50}\n{:^50}\n{:^50}\n".format('~'*30, "Welcome to Abdul's Game Hub!", '~'*30))
    print("{:^50}\n{}\n\n{:^50}".format('*'*60,"In here, you have the opportunity to play through 3 games I have created! Below are the choices of the games I've made!\n\nEnjoy!",'*'*60))

    # Ask for user's input
    user = input("\nSelect from three games available!\n(Enter the list number or the first word of the list)\n\n1) Quiz Game\n2) Card Game\n3) Guessing Game\n4) Exit the Hub\n\n>> ").lower()

    if (user == '1' or user == "quiz"):
        print("You have chosen the Quiz Game!\n")
        time.sleep(1)
        Quiz.quiz()

    elif (user == '2' or user == "card"):
        print("You have chosen the Card Game!\n")
        time.sleep(1)
        HigherOrLower.card()

    elif (user == '3' or user == "guess" or user == "guessing"):
        print("You have chosen the Guessing Game!\n")
        time.sleep(1)
        Hangman.guess()

    elif (user == '4' or user == 'quit' or user == 'exit'):
        for x in range (0,4):
            b = "Leaving Game Hub" + "." * x
            print (b, end="\r")
            time.sleep(0.5)
        sys.exit()

    elif (user.isalpha()):
        print("I don't speak Jibberish!")
        time.sleep(1)
        continue

    else:
        print("Invalid Range!\n")
        time.sleep(1)
        continue

########################################### END OF INTERFACE #####################################################################
