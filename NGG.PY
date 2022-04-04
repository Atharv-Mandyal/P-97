import random 

print("number guessing game")
#This function is to generate numbers etween 1 to 9
number = random.randint(1,9)
chances = 0
print("guess a number between 1 to 9:")
while chances <5:
    guess=int (input("enter your guessed number"))
    if number==guess:
        print("your GUess Was Right")
    elif number>guess:
        print("your number is greater than your guesses",guess)
    else :
        print("your number is smaller than your guesses",guess)
    chances+=1
#check whether the user guessed the correct number
if not chances<5:
    print("you lost the game the number is:", number)
