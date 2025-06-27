import day12_projectLogo
import random

def attempts_number(level):
    attempts = (10 if level == "easy" else 5)
    print(f"You have {attempts} attempts remaining to guess the number.")
    return attempts

def guess_process(attemps):
    for i in range(1,attemps + 1):
        guess_number = int(input("Make a guess: "))
        if guess_number == number:
            print(f"You got it! The answer was {number}.")
            return True
        elif guess_number < number:
            print(f"Attempt {i}: Your guess is {guess_number}.")
            print("Too low.")            
        else:
            print("Too high.")
            print(f"Attempt {i}: Your guess is {guess_number}.")
    return False

print(day12_projectLogo.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
message = (f"You guessed the number: {number}" if guess_process(attempts_number(difficulty)) else f"You Lost the number was {number}.")
print(message)








