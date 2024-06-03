#it is an encryption and decryption of WORD which we give to encode or decode
#we also give SHIFT NUMBER so that it can shift that many alphabets
'''EXAMPLE: 
type encode or decode
give text
give shift number
encoded type

encode
Hello world!
9
encoded type: qnuux gxbum!
'''

#import logo of caesar cipher

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
          "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
            shift_amount *= -1
    for letter in start_text:
        #if user enters a number or symbol or space they should be same
      if letter in alphabet:
        position=alphabet.index(letter)
        new_position=position+shift
        new_letter=alphabet[new_position]
        end_text+=new_letter
      else:
          end_text+=letter
    
    print(f"The {cipher_direction}d text is: {end_text}")
    
game_running=True 
while game_running:
 direction=input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
 text=input("Type your message: ").lower()
 shift=int(input("Type the shift number: "))
 
 shift=shift%25
 
 caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
        
 result=input("if you want to run the game again Type 'yes' or Type 'no' if you don't want: ").lower()

 if result=="no":
    game_running=False

   

    
    
    
     