import random


magic_number = random.randint(0, 100)
while True:
    guess = int(input("Guess: "))

    if guess < magic_number:
        print("Greater")
    elif guess > magic_number:
        print("Lower")
    else:
        print("You guessed it!")
        break


