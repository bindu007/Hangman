import random

from Hangman_word_list import word_list
from Hangman_ascii_art import stages
from Hangman_ascii_art import logo

print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
 
#lives to equal 6.
lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: \n").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
      lives = lives-1
      if lives == 0:
        end_of_game = True
        print("\nyou loose!")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(f"remaining lives are {lives}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])