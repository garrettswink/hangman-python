# Module imports
import random
import os

# File imports
from art import logo, stages
from words import word_list

# Create the clear function
def clear():
    os.system('clear')

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

# 🔥🔥🔥 Add the while loop + clear function as last step 🔥🔥🔥

guess = input("Guess a letter: ").lower()

if guess in display:
    print(f"You have already guessed {guess}! Please try again.")



for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        print(f'The letter {guess} is in the word!')