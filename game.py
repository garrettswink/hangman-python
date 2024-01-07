# Module imports
import random
import os

# File imports
from art import logo, stages
from words import word_list

# Create the clear function
def clear():
    os.system('clear')

# Wrap this whole bad boy in a function for replay
def playgame():

    print(logo)

    # Select a random word using the random module
    chosen_word = random.choice(word_list)
    # The below f string is for testing purposes + should be
    print(f'The generated word is {chosen_word}.')

    # Set the number of tries before game over
    # The imported stages list holds seven pieces of ASCII art, so we set the tries to six. 
    tries = 6

    # Create an empty list to hold the game's word display
    display = []

    # Convert the chosen_word string to the the number of letters
    word_length = len(chosen_word)

    # Use a for loop and the range function to generate an underscore for each
    # Letter of the randomly generate word within the list display 
    for _ in range(word_length):
        display += "_"
    print(display)

    # Define end_of_game for the below while loop
    end_of_game = False

    while not end_of_game: 
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"You have already guessed {guess}! Please try again.")


        # We create another for loop that iterates through each index of the word stored in word_length with the range function
        # Inside the loop, letter = chosen_word[position] gets the letter at the current index (position) of chosen_word.
        # The "if letter == guess" statement then checks if this letter matches the player's guess.
        # If the letter and the guess do match, the display position is updated with the letter
        # And the letter is printed in the f string
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print(f'The letter {guess} is in the word!')
        
        # Print the updated display
        print(display)

        # This is pretty straight forward.
        # However, reviewing this highlighted that there are different ways of writing this program.
        # For example, instead of the above for loop, I could do "if guess in chosen_word:"
        # And use an else statement to handle a wrong letter.
        if guess not in chosen_word:
                print(f"The letter {guess} is not in the word.")
                tries -= 1
                if tries == 0:
                    end_of_game = True
                    print("You lose!!!")
        
        # The below joins the lives countdown to the stages ascii art and prints accordingly
        print(stages[tries])

        if "_" not in display:
            end_of_game = True
            print("You win!!!")

        if end_of_game:
            play_again = input("Would you like to play again? (y/n): ").lower()
            if play_again == 'y':
                clear()
                playgame()
            elif play_again == 'n':
                print("Thanks for playing!")
                break

playgame()

