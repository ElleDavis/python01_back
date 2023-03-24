#guessing game 01

#generate a random Number
import random
random=(random.randrange(11))
#user guesses
guess1= input ("Guess what number im thinking between 0-10 .. ")
#correct or no
if guess1 == random :
    print("correct")
else print("guess again")
#print(random.randrange(11))
#user Guesses
#endpoint