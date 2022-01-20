################# IMPORTING ALL LIBRARIES #################
import sys
import random
import os
import time

################# IMPORTING LOCAL MODULES #################
from hangmanWords import words # Adapted from https://www.youtube.com/watch?v=cJJTnI22IF8

################# END OF IMPORTING #################

########################################### START OF HANGMAN #####################################################################
def guess():
    os.system('cls')

################# START OF RULES #################
    # Some sort of graphics in the terminal with rules of game
    print("{:^50}\n{:^50}\n{:^50}\n".format('+'*30, "Welcome to The Hangman Game!", '+'*30))
    print("{:^50}\n{}\n\n{:^50}".format('*'*70,"In this game, you have 12 tries to guess a word that I am thinking. You can either guess by typing a Letter or typing a Word. However, if you try to guess a word and it's incorrect, then you lose 2 turns! If you guess an incorrect letter, you will lose 1 turn. Your goal to try and guess the word I am thinking before you run out of tries!\n\nGood Luck!",'*'*70))
################# END OF RULES #################

    # Adapted from https://www.youtube.com/watch?v=cJJTnI22IF8
    def validWord(arg):
        word = random.choice(arg)           # Chooses a random word from the list
        while '-' in word or ' ' in word or len(word)<=3:           # Keeps looping through the word list until it finds a word without a space or dash
            word = random.choice(arg)           # Picks random word again
        return word         # Return the random word

################# START OF WHILE LOOP #################
    # Ask user if they want to play the game or add words to the word bank
    while (True):
        choice = input("\nDo you want to add a word to the bank or play?\n1) Add a word\n2) Play\n3) Exit Game\n\n>> ").lower()

        if (choice == "1" or choice == "add"):          # If they want to add words to the bank
            while (True):
                add = input("\nType in the word you want to add\n\n>> ").lower()
                if (add in words):            # If the word already exists in the bank, then ignore it
                    print("\nSorry, that word already exists in the word bank!")
                    continue

                elif(add.isdigit()):            # If user entered a number, then ignore it
                    print("No numbers!")
                    continue

                elif (len(add) >= 4):           # If length of the word is more than or equal to 4
                    words.append(add)            # Then add the word to the bank
                    print(f"\nYour word '{add}' was successfully added to the word bank!")
                    break           # Break out of the loop

                else:           # Anything else, print following statement
                    print("Length of the word has to be 4 or greater!")
                    continue

        elif (choice == "2" or choice == "play" or choice == ""):           # If user wants to play
            print("\nLets Go!")
            break           # Break out of the loop

        elif (choice == "3" or choice == "exit"):
            for x in range (0,4):
                b = "Leaving Hangman Game" + "." * x
                print (b, end="\r")
                time.sleep(0.5)
            os.system('cls')
            return ""           # Returns to the main page

        else:
            print("Invalid Option!")
            continue
################# END OF WHILE LOOP #################

    # Taken from https://stackoverflow.com/questions/5290994/remove-and-replace-printed-items
    for x in range (0,4):
        b = "Starting Game" + "." * x
        print (b, end="\r")
        time.sleep(0.5)
    os.system('cls')

################# DEFINING VARIABLES #################
    randomWord = validWord(words)            # Choosing a random word
    lenWord = len(randomWord)           # Finding length of the word
    lettersUsed = []            # Creating empty list where letter guesses will be stored
    wordsUsed = []          # Creating empty list where word guesses will be stored

    turns = 12           # Defining number of turns
    correct = 0         # Counter for how many times user guesses right
    guessed = True         # Boolean for while loop
################# END #################

    # Taken idea from https://stackoverflow.com/questions/33890590/how-to-replace-the-underscores-with-chosen-letters-in-hangman
    displayUnderscore = ([" _ "]*lenWord)           # Create an '_' for every letter in the word
    print(f"Length of your word is {lenWord} and is also represented with underscores below:\n")            # Letting user know length of word
    for i in displayUnderscore:
        print(i, end='')            # Prints underscores

################# START OF WHILE LOOP #################
    while(turns!=0 or guessed):            # Setting condition, if guessed is not False or if turns is not equal to 0
        userGuess = input("\n\nGuess a Letter or a Word\n>> ")            # Ask user to guess a letter or word
        lenGuess = len(userGuess)         # Variable for length of user input to use later

        for index, letter in enumerate(randomWord):
            if (letter == userGuess):
                displayUnderscore[index] = userGuess            # Replacing underscore with letter if guessed correctly
        underscoreFilled = ''.join([x for x in displayUnderscore])          # Converts list of underscore into string
        print(underscoreFilled)         # Displays the underscores with letters, if letter guessed is in the random word

        if (userGuess.isdigit()):           # Checks if user entered a number
            print("\nOnly Letters or Words Please!")
            continue            # If so, ignore it

        elif (userGuess in lettersUsed):            # Checks if user guessed the same letter more than once
            print(f"\nYou've already guessed the letter '{userGuess}'\nTry a different letter!")
            continue            # If so, let them know and ignore it

        elif (userGuess in wordsUsed):          # Checks if user guessed the same word more than once
            print(f"\nYou've already guessed the word '{userGuess}'\nTry a different word or letter!")
            continue            # If so, let them know and ignore it

        elif (lenGuess == 1 and userGuess in randomWord):           # If user guesses correct letter
            correct += 1            # Increments correct variable by 1
            lettersUsed.append(userGuess)           # Add letter to the 'lettersUsed' list

        if (correct == lenWord or userGuess == randomWord or underscoreFilled == randomWord):           # If the user guesses word correct or correct variable is equal to length of word or if the underscoreFilled variable is equal to word
            print(f"\nCongrats! You guessed the word correctly!\nIt was '{randomWord}'!")           # Let user know they won the game!
            print(f"\nYou had {turns} tries left!\n")           # Show how much turns they had left before failure

        ################# ADDING TO TEXT FILE #################
            f = open('Scores.txt', 'a+')
            f.write(f"\nYou guessed the word correct and had {turns} turns left!\nThe word was '{randomWord}'")
            f.close()
        ################# END OF ADDING TO TEXT FILE #################

            guessed = False           # Break out of the loop
            break

        elif (lenGuess == 1 and userGuess not in randomWord):         # Statement whenever the letter guessed is not in the word
            turns -= 1          # If so, then take away 1 turn
            if (userGuess not in lettersUsed):          # Checks if letter is not already used
                lettersUsed.append(userGuess)           # If not, then add to the list
            elif (turns <= 0):            # Checking if user ran out of turns
                break           # If so, break the loop
            print(f"\nThe letter '{userGuess.upper()}' is not in the secret word!\nYou now have {turns} turns left!")           # Tells user letter is incorrect and displays amount of tries left

        elif (lenGuess > 1):            # Checking if length of user input is more than 1
            wordsUsed.append(userGuess)         # Adding guessed word to the 'wordsUsed' list
            if (userGuess != randomWord):           # Checks if the word guessed is not equal to the word
                turns -= 2          # If so, then take away 2 turns
                if (turns <= 0):            # Checking if user ran out of turns
                    break               # If so, break the loop
                print(f"\n'{userGuess}' was not the word I was thinking of!")           # Lets user know that the word was incorrect
                print(f"\nTaking away 2 turns for guessing a word incorrectly!\nYou now have {turns} turns left!")            # Let user know they lost 2 turns for guessing an incorrect word

        if (len(lettersUsed) > 0):          # Outputs a list of all the letters the user used
            print("\nLetters guessed soo far:", lettersUsed)
        if (len(wordsUsed) > 0):            # Outputs a list of all the words the user used
            print("Words guessed soo far:", wordsUsed)

        if (turns <= 0):
            break

################# END OF WHILE LOOP #################


    # Only prints below statement if user runs out of turns
    if (turns <= 0):
        print(f"\nWhoops! You Ran Out of Turns!\nBetter Luck Next Time!\n\nThe word I was thinking was: '{randomWord}'")
    ################# ADDING TO TEXT FILE #################
        f = open('Scores.txt', 'a+')
        f.write(f"\nYou didn't guess the word! It was '{randomWord}'")
        f.close()
    ################# END OF ADDING TO TEXT FILE #################

    # Lets user know what letter's and words they used in the game
    if (len(lettersUsed) > 0):
        print("All the letters you used are", lettersUsed)
    if (len(wordsUsed) > 0):
        print("All the words you used are", wordsUsed)
    elif (len(wordsUsed) == 0):
        print("You didn't guess any words")

    # Let user know the game is over and exiting game
    print("\nGAME OVER!\n")
    for x in range (0,4):
        b = "Exiting Hangman" + "." * x
        print (b, end="\r")
        time.sleep(0.5)
    time.sleep(8)
########################################### END OF HANGMAN #####################################################################

# Adapted from https://stackoverflow.com/questions/6523791/why-is-python-running-my-module-when-i-import-it-and-how-do-i-stop-it
if __name__ == "__main__":
    guess()
