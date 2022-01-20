################# IMPORTING ALL LIBRARIES #################
import sys
import random
import os
import time
################# END OF IMPORTING #################

########################################### START OF HIGHER OR LOWER #####################################################################
def card():
    os.system('cls')

################# START OF RULES #################
    # Some sort of graphics in the terminal
    print("{:^50}\n{:^50}\n{:^50}\n".format('+'*40, "Welcome to Higher or Lower Card Game!", '+'*40))
    print("{:^50}\n{}\n\n{:^50}".format('*'*70,"Higher or Lower is a card game where you get given the first card and you must guess whether the next card's value is higher or lower than your current card. You must be able to guess all of the cards correct simultaniously in order to win the game! If you guess wrong once, you lose the game! Try and guess all 8 cards correct!\n\nGood Luck!",'*'*70))
################# END OF RULES #################

    # Ask user if they're ready to start the game
    startGame = input("Start Game? (y/n)\n>> ").lower()
    if (startGame == "yes" or startGame == "y" or startGame == ""):        # If they answer yes/y or press enter then clear the terminal and start the game
        for x in range (0,4):
            b = "Starting Game" + "." * x
            print (b, end="\r")
            time.sleep(0.5)
        os.system('cls')
    else:           # Otherwise exit the card game
        for x in range (0,4):
            b = "Leaving Card Game" + "." * x
            print (b, end="\r")
            time.sleep(0.5)
        os.system('cls')
        return ""           # Returns to the main page

################# CREATING THE CARD DECK #################
    # Creating lists for the suits and card ranks
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
    rank = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']

    deck = []   # Declare an empty list

    # Created a function where I use for loops to create a full deck of cards
    def createDeck():
        cardValue = 1     # Create a counter to add a value to each card
        for i in rank:
            for j in suits:     # Nested for loop to iterate through each rank with suits
                deck.append([str(i) + " of " + j, cardValue])     # Append the cards to the deck list with its value
            cardValue += 1        # Increment the counter by 1 each time it iterates through a new set of cards
################# END OF CREATING DECK #################

    createDeck()        # Run the function
    random.shuffle(deck)        # Shuffle the deck

    nineCards = random.sample(deck, 9)      # Select 9 random cards from the deck
    newDeck = [x for x in nineCards]        # Create new list and add the 9 cards to the list

    print('\n')     # New line

    print("Here are your list of cards!\n")
    for cards in newDeck:
        print('X')      # Print the length of the 9 cards with letter 'X'

    score = 0       # Create a score variable for the scoring system
    if (newDeck[0][1] == newDeck[1][1]):      # Check if the value of the cards are the same. If it is, end the game
        print("\nCard is repeated...")
        # Print below shows the first and second card to the user to show that the cards have same value and shows their score
        print(f"First card was {newDeck[0][0]} and second card was {newDeck[1][0]}\nYour score was: {score}\n\n")
        for x in range (0,4):
            b = "Ending Game" + "." * x
            print (b, end="\r")
            time.sleep(0.5)
        return ""      # Exits the game

    # Shows the user the first card from the 9 random cards
    print(f"\nThe first card is {newDeck[0][0]}")

################# START OF WHILE LOOP #################
    while(score != 8):      # While condition is if the score is not equal to 8
        userInput = input("Is the next card Higher or Lower?\n>> ").lower()     # Ask the user if next card is higher or lower

        if (userInput == 'higher' or userInput == 'h') and (newDeck[1][1]>=newDeck[0][1]):      # If the user guessed higher and next card value is greater than current card
            if (newDeck[0][1] == newDeck[1][1]):        # If the current card and next card has same value, then print this and carry on
                print("\nCards have the same value, but I'll let you off!")
            newDeck.pop(0)      # Remove first card from the list
            print(f"\nCorrect it is Higher!\n\nYour next card is {newDeck[0][0]}")       # Let user know they're correct and show them the next card
            score += 1      # Increment score by 1


        elif (userInput == 'lower' or userInput == 'l') and (newDeck[1][1]<=newDeck[0][1]):     # If the user guessed lower and next card value is less than current card
            if (newDeck[0][1] == newDeck[1][1]):         # If the current card and next card has same value, then print this and carry on
                print("\nCards have the same value, but I'll let you off!")
            newDeck.pop(0)      # Remove first card from the list
            print(f"\nCorrect it is Lower!\n\nYour next card is {newDeck[0][0]}")        # Let user know they're correct and show them the next card
            score += 1      # Increment score by 1

        # Otherwise let user know they're incorrect and show the next card. Break out of the loop
        else:
            print(f"\nUnlucky! The card was {newDeck[1][0]}")
            break
################# END OF WHILE LOOP #################

################# PRINT STATEMENTS #################
    # If statements to print certain messages according to the users score
    if (score == 8):
        print(f"\nYou Score is: {score}/8!\nCongrats! You have completed the Higher or Lower card game!")
    elif (score >= 5):
        print(f"\nYou Score is: {score}/8!\nOh no! Soo close! Better luck next time!")
    elif (score ==  4):
        print(f"\nYou Score is: {score}/8!\nNooo! You were half way through! Play again and get higher!")
    elif (score < 4):
        print(f"\nYou Score is: {score}/8!\nPoor! You could do a lot better than that!")
################# END OF PRINT STATEMENTS #################

################# ADDING SCORE TO A TEXT FILE #################
    f = open('Scores.txt', 'a+')
    f.write(f"\nYour score for the Higher or Lower Card Game was {score}/8")
    f.close()
################# END OF ADDING SCORE TO A TEXT FILE #################

    # Let user know the game is over and exiting game
    print("\nGAME OVER!\n")
    for x in range (0,4):
        b = "Exiting Card Game" + "." * x
        print (b, end="\r")
        time.sleep(0.5)
    time.sleep(5)
########################################### END OF HIGHER OR LOWER #####################################################################

if __name__ == "__main__":
    card()
