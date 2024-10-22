#####Guess the number#####

import random

random_number = random.randint(1,10)
guesses = 0

while guesses < 3:
    user_guess = int(input("Please guess a number 1-10: "))
    if  user_guess == random_number:
        print("You guessed the number right!")
        guesses=4
    elif user_guess > random_number:
        print("Your number is too large")
        guesses += 1
    elif user_guess < random_number:
        print("Your number to too small")
        guesses += 1

if guesses == 3:
    print("You ran out of gueeses")