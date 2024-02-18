#import random to enable random choice
import random
#import os to enable clearing of console
import os
#define logo 
logo = """   _____                       _   _                                  _               _ 
  / ____|                     | | | |                                | |             | |
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __| |
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| |
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |  |_|
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  (_)
                                                                                         """
                                                                                       

#Define a function used to determine the difficult of the game
#Difficulty determines amount of guesses for user
def difficulty():
    '''Classify the difficulty the user wants to play on'''
    #Ask the user for an input of easy or hard mode
    difficulty = input("Choose a difficulty. Type 'e' for easy or 'h' for hard! ").lower()
    
    #If easy, give 10 guesses
    if difficulty == "e":
        amount_of_guesses = 10
        print ("You have chosen easy mode, You have 10 guesses ")
        return amount_of_guesses
    #if hard, give 5 guesses
    elif difficulty == "h":
        amount_of_guesses = 5
        print ("You have chosen hard mode, You have 5 guesses ")
        return amount_of_guesses
    #if invalid input, give the user 10 guesses
    else:
        amount_of_guesses = 10
        print("Incorrect input, we have given you the easy mode, 10  guesses! ")
        return amount_of_guesses

#Define a function that will play the game
def guessing_game():
    '''The number guessing game'''
    #Print the welcoming text and logo
    print (logo)
    print ("Welcome to the Number Guessing Game! ")
    print ("I'm thinking of a number between 1 and 100. ")
    #Amount of guesses is based on the input to the difficulty function
    amount_of_guesses = difficulty()
    #Choose a random number betweewn 1 and 100
    random_number = random.choice(range(1,101))
    # for test purposes remove the # for the line below: 
    #print (f"The number is {random_number}")
    # define boolean for the while loop
    stop_playing = False
    # Ask user for the first guess
    guess = int(input("Guess a number betweewn 1 and 100: "))
    # while loop for guessing
    while not stop_playing:
        #If user is out of guesses, and has not guessed the number, 
        #tell them they ran out and stop the loop
        if amount_of_guesses == 1 and guess != random_number:
            print("You ran out of guesses!")
            stop_playing = True
        #if their guess is out of the range, tell them, do not remove a guess
        elif guess > 100 or guess < 1:
            print ("The number is between 1 and 100, you guess out of the range, try again. ") 
            print (f"You dont lose a life. You have {amount_of_guesses} guesses left! ")
            guess = int(input("Guess a number betweewn 1 and 100: "))
        #if the guess is higher than the random number, tell them and ask again, lose a life
        elif guess > random_number:
            print ("Too high, guess again! ")
            amount_of_guesses -= 1
            print (f"You have {amount_of_guesses} guesses left! ")
            guess = int(input("Guess a number betweewn 1 and 100: "))
        #if the guess is lower than the random number, tell them and ask again, lose a life    
        elif guess < random_number:
            print("Too low, guess again! ")
            amount_of_guesses -= 1
            print (f"You have {amount_of_guesses} guesses left! ")
            guess = int(input("Guess a number betweewn 1 and 100: "))
        #if the guess is correct, tell them and stop the loop
        elif guess == random_number:
            print ("Congratulations you guessed the number! ")
            stop_playing = True

#play the game    
guessing_game()
#new boolean for new loop
finished = False
#Ask the user if they want to play again
while not finished:
    #If they say no to playing again, then finish loop
    if input("Type 'y' to go again, or 'n' to stop playing: ").lower() != "y":
        finished = True
    #otherwise clear the console and play the game again    
    else:
        os.system('cls')
        guessing_game()