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

# Determine the number of letters in each word (i.e. length of each word)
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"
print(display)





