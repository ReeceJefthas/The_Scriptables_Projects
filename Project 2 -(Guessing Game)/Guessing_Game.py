#import for a random number
import random
#to generate a random number
number = random.randint(1, 50)
print("Im thinking of a number between 1 and 50 ")
guessesTaken = 0
#how much guesses they can have

while guessesTaken < 6:
    guess = input("Enter a guess: ")
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print("That was too low.")
    elif guess > number:
        print("That was too high")
    else:
        break

if guess == number:
    print("U win")
else:
    print("U lose better luck next time")


