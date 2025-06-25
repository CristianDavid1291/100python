import random

print("what do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors")

choice_list = ["Rock", "Paper", "Scissors"]

user_choice = choice_list[int(input("Enter your choice: "))]

random_choice = random.choice(choice_list)

print(f"You chose: {user_choice}, Computer chose: {random_choice}")

if user_choice == random_choice:
    print("It's a draw!")
elif (user_choice == "Rock" and random_choice == "Scissors") or \
     (user_choice == "Paper" and random_choice == "Rock") or \
     (user_choice == "Scissors" and random_choice == "Paper"):
    print("You win!")
else:
    print("You lose!")





