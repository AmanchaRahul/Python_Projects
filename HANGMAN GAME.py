#HANGMAN GAME

#So, it is a Simple code where at last we need to save a person(diagram) from hanging 
# by providing the exact words in the filling in the blanks
#as we give wrong letter it keeps on drawing

'''So, game runs in a way where 
STARTS WITH: Guessing a letter: 
1. if we give correct word then it won't draw diagram
2. else it would draw diagram one by one'''

import random

from hangman_words import word_list
from hangman_art import logo

stages = ['''
  +---+
  |   |
  O   |                    #stages[lives]==stages[0]
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |                    #stages[lives]==stages[1]
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |                    #stages[lives]==stages[2]
      |
      |
=========
''', '''
  +---+
  |   |
  O   |                    #stages[lives]==stages[3]
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |                    #stages[lives]==stages[4]
      |
      |
=========
''', '''
  +---+
  |   |
  O   |                    #stages[lives]==stages[5]
      |             
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |                   #stages[lives]==stages[6]
      |
      |
=========
''']


end_of_game=False


#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
print(chosen_word)


#Create a Variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal to 6

lives=6

print(logo)
#Create an empty list called display. for each letter in chosen_word, add a "-" to 'display'
#So, if the chosen_word is "messi", display should be ["-","-","-","-","-"]
display=[]
for _ in range(len(chosen_word)):
    display+="-"
print(display)



'''Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters
in the chosen_word and "display" has no more blanks(-). Then you can tell the user they've won.
if the user doesn't guess in 6 attempts then tell the user he lose'''

while not end_of_game:
#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess=input("Guess a letter: ").lower()


#Loop through each position in the chosen_word:
#if the letter at that position matches 'guess' the reveal that letter in the display at that position.
#if user guessed "s" and choosen_word was "messi", then display should be ["-","-","s","s","-"]


    for pos in range(len(chosen_word)):
      letter=chosen_word[pos]
      if letter==guess:
        display[pos]=letter
        
  #  if guess is not a letter in the chosen_word, then reduce 'lives' by 1.
  #  if lives goes down to 0 then game should stop and it should print "you lose" 
 
    if guess not in chosen_word:
     lives-=1
     if lives==0:
         end_of_game=True
         print("you lose")
         
    
    print(' '.join(display))     
         
 
     
    if "-" not in display:
     end_of_game=True
     print("you won")
     
    print(stages[lives])
