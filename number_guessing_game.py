# Number Guessing Game between 1 and 99

import random

numberOfAttempts = int(0)
numberToGuess = random.randrange(1, 100)
exitState = False

hintWhileState = False
hintState = None

while hintWhileState == False:
    hintInput = str(input("Do you want to enable hints? YES [Y] or NO [N]: "))
    if hintInput in ['y', 'yes', 'YES', 'Y']:
        hintState = True
        hintWhileState = True
    elif hintInput in ['n','no', 'No', 'N']:
        hintState = False
        hintWhileState = True
    else:
        print(f"Invalid input! Please enter [Y] or [N]")

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
        if hintState == True:
            if userNumberGuess < numberToGuess:
                print(f'Your guess is too LOW, guess a bigger number')
            if userNumberGuess > numberToGuess:
                print(f'Your guess is too HIGH, guess a smaller number')
        else:
            continue
    