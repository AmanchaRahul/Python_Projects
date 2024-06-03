import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]

user_input=int(input("enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_input=random.randint(0,2)

 
if user_input>=0 and user_input<=2:
     print("You Choose:",game_images[user_input])
     print("Computer choose:",game_images[computer_input])
     if user_input==computer_input:
        print("it's a draw")
     elif user_input==0 and computer_input==2:
        print("You win")
     elif user_input==1 and computer_input==0:
        print("you win")
     elif user_input==2 and computer_input==1:
        print("you win")
     else:
        print("You lose")   
else:
     print("Invalid option!")     
    