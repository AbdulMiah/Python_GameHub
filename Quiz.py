################# IMPORTING ALL LIBRARIES #################
import time
import os

################# IMPORTING LOCAL MODULES #################
from quizQuestions import allQuestions

################# END OF IMPORTING #################

########### REFERENCE ###########
# https://stackoverflow.com/questions/54294572/accessing-same-keyvalue-pair-in-list-of-dictionaries-in-python
#################################


########################################### START OF QUIZ #####################################################################
def quiz():
    os.system('cls')

################# START OF RULES #################
    # Some sort of graphics in the terminal
    print("{:^70}\n{:^70}\n{:^70}\n".format('+'*50, "Welcome to the General Knoweledge Quiz Game!", '+'*50))
    print("{:^70}\n{}\n\n{:^70}".format('*'*70,"In this general knowledge quiz, you will be prompted with Ten questions with multiple choices. Your goal is to answer all questions correct in order to win! Are you the General Knowledge King?\n\nGood Luck!",'*'*70))
################# END OF RULES #################

    # Ask user if they're ready to start the game
    startGame = input("Start Game? (y/n)\n>> ").lower()
    if (startGame == "yes" or startGame == "y" or startGame == ""):        # If they answer yes/y or press enter then clear the terminal and start the game
        for x in range (0,4):
            b = "Starting Game" + "." * x
            print (b, end="\r")
            time.sleep(0.5)
        os.system('cls')
    else:           # Otherwise exit the game
        for x in range (0,4):
            b = "Leaving Card Game" + "." * x
            print (b, end="\r")
            time.sleep(0.5)
        os.system('cls')
        return ""           # Returns to the main page

################# DECLARING SOME VARIABLES #################
    myQues = []
    myAns = []
    myOpt = []
    score = 0

    # Adding the questions, answers and options to separate lists
    for i in allQuestions:
        myQues.append(i['ques'])            # Adds the keys with name 'ques' to the 'myQues' list
        myAns.append(i['ans'])            # Adds the keys with name 'ans' to the 'myAns' list
        myOpt.append(i['opt'])            # Adds the keys with name 'opt' to the 'myOpt' list

    def newOptions():           # Declare a function where the index of the options will be replaced with letters (A, B, C, D)
        letters = 'A', 'B', 'C', 'D'            # The letters to replace index
        for index, options in enumerate(myOpt[0]):          # Using enumerate to get the index of the options
                print(letters[index],')', options)          # Replace the index with letters

################# START OF FOR LOOP #################
    for questions in myQues:
        print('\n'+questions+'\n')          # Prints the questions
        newOptions()            # Prints the options

        # Ask user for their answer
        user = input("\n>> ").lower()

        if (user == myAns[0][0] or user == myAns[0][1]):            # Checks if user answer is equal to the correct answer
            print("\nThat is Correct!\n+1 Point")           # If so, let user know they're correct
            myAns.pop(0)            # Remove the answer from the list
            myOpt.pop(0)            # Remove the option from the list
            score += 1          # Increments score by 1
        else:           # If anything else
            print(f"\nIncorrect! The answer was {myAns[0][1].upper()}) {myAns[0][0].capitalize()}")         # Let user know they were incorrect and show answer
            myAns.pop(0)            # Remove the answer from the list
            myOpt.pop(0)            # Remove the options from the list
            continue            # Ignore the input
################# END OF FOR LOOP #################

################# PRINT STATEMENTS #################
    # If statements to to print certain messages according to the users score
    if (score == 10):
        print(f"\nCongrats you won! You answered all questions correct!\nYour score is {score}/10")
    elif (score > 5):
        print(f"\nOh no you were soo close!\nYour score is {score}/10")
    elif (score == 5):
        print(f"\nYou were half way there! Better luck next time!\nYour score is {score}/10")
    elif (score < 5):
        print(f"\nVery poor general knowledge! You can do a lot better than that!\nYour score is {score}/10")
################# END OF PRINT STATEMENTS #################

################# ADDING SCORE TO A TEXT FILE #################
    f = open('Scores.txt', 'a+')
    f.write(f"\nYour score for the General Knoweledge Quiz was {score}/10")
    f.close()
################# END OF ADDING SCORE TO A TEXT FILE #################

    # Let user know the game is over and exiting game
    print("\nGAME OVER!\n")
    for x in range (0,4):
        b = "Exiting Quiz Game" + "." * x
        print (b, end="\r")
        time.sleep(0.5)
    time.sleep(5)
########################################### END OF QUIZ #####################################################################

if __name__ == "__main__":
    quiz()
