Author: Ivan Wu
Date: March 6th, 2024
Time spent on the project: ~30 minutes
Language(s) project was made in: Python

How I made this Project:

1. I imported the random library in order to create a 
    random generated number

2. I created the variable numberOfAttempts to keep track 
    of how much numbers were guessed

3. I created the variable numberToGuess to denote the number which 
    needs to be guessed by the user

4. I created the variable exitState to control the 
    state of the while loop

5. I created the game within a while loop to loop 
    infinitely until the user guesses the right answer

6. Within the while loop we have several conditional statements:
    a. The first conditional statement runs if the guessed number 
        is equal to the randomly generated number. This code simply
        changes the exitState to denote the end of the while loop, which
        essentially ends the game and then it prints out a couple statements 
        showing a "win" statement, the number of the user's guess and 
        how much attempts were needed

    b. The second conditional statement runs if the guessed number is not
        equal to the randomly generated number. The exitState is not changed,
        which continues the loop, essentially prolonging the game.
        As a hint to the users, additional contitional statements print out 
        whether the users' guess was higher or lower than the randomly generated 
        number.


Extra: I added an option to enable hints or disable hints. 
        I implemented this by using yet another variable to control
        the state of whether the user wants hints or not. Before the game   
        even starts, the user gets a prompt whether they'd like to
        enable cheats or not. Based off the users' input, hints can be 
        enabled or disabled. Before displaying hints in the conditional 
        of 6b, a conditional statement checks to see if the hintState is 
        true or false, and then either displays hints or not accordingly.