"""
Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. 
This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""

from random import randint

print("Hello! What is your name?")
name = input()
print("Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")

guessedNumber = randint(1, 20)

steps = int(0)
guess = int()
while ( guess != guessedNumber ):
    guess = int(input())
    if ( guess < guessedNumber ):
        print( "Your guess is too low." )
        steps += 1
        continue
    elif ( guess > guessedNumber ):
        print( "Your guess is too high." )
        steps += 1
        continue

print ("Good job, {0}! You guessed my number in {1} guesses!".format(name, steps))

