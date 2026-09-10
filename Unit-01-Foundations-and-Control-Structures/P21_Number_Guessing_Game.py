import random

number = random.randint(1, 100)
guess = None
while number != guess:
    guess = int(input("Enter your guess (between 1 and 100): "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    
    if guess == number:
        print("Congratulations! You've guessed the correct number:", number)