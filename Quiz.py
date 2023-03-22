#Greet user
greeting="Welcome to my Quiz!"
print(greeting)

#Ask User if they want to play
playing= input("Would you like to take my quiz? ")
print(playing)

#Start Tracking Score
score=0

#Did the User say Yes or no ?
if playing.lower() != "yes":
    quit()
print("Okay, Let's Play!")

#Ask Question 
question= input("Which month has the fewest days? ").lower()
print(question)

#Check User answer 1
if question == "february":
    print("Correct")
    score +=1
else:
    print("Incorrect")

#Ask Question 
question= input("Is 2 an even number? ").lower()
print(question)

#Check User answer 2
if question == "yes":
    print("Correct")
    score +=1
else:
    print("Incorrect")
   
#Ask Question 
question= input("Is 3 an even number? ").lower()
print(question)

#Check User answer 3
if question == "no":
    print("Correct,Nice!")
    score +=1
else:
    print("Incorrect")
   
#Ask Question 
question= input("Is green a primary color? ").lower()
print(question)

#Check User answer 4
if question == "no":
    print("Correct, Great Job")
    score +=1
else:
    print("Incorrect")

#Give user a score
print("You Got " + str(score)+ " questions correct")
print("You Got" + str((score/4)* 100) + "%")