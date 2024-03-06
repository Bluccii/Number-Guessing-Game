# Number Guessing Game between 1 and 99

import random

numberOfAttempts = int(0)
numberToGuess = random.randrange(1, 100)
exitState = False

while exitState != True:
    userNumberGuess = int(input("Enter your guess!: "))
    numberOfAttempts += 1 
    if userNumberGuess == numberToGuess:
        exitState = True
        print(f"----------------------------------------------------------------")
        print(f"Your answer is correct")
        print(f"Your guess of {userNumberGuess} is the random number, {numberToGuess}")
        print(f"It took you {numberOfAttempts} attempts!")
    if userNumberGuess != numberToGuess:
        if userNumberGuess < numberToGuess:
            print(f'Your guess is too LOW, guess a bigger number')
        if userNumberGuess > numberToGuess:
            print(f'Your guess is too HIGH, guess a smaller number')
    