#password generator


#we want alphabets,numbers,special characters,length
import random

alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
special_characters="!@#$%&()*+"

password=""

n_alphabets=int(input("how many alphabets you want? "))
n_numbers=int(input("how many numbers you want? "))
n_special_char=int(input("how many special characters you want? "))

for i in range(1,n_alphabets+1):
    char=random.choice(alphabets)
    password+=char
    
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char
    
for i in range(1,n_special_char+1):
    char=random.choice(special_characters)
    password+=char


password_as_list=list(password)

    

print("Password before shuffled:",password_as_list)
random.shuffle(password_as_list)
print("Password after shuffled:",password_as_list)


generated_password=""
for char in password_as_list:
    generated_password+=char
    
print("Generated Password is:",generated_password)

