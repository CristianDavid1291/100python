import art
import bd
import random

print(art.title)
#get random dictionary key
bd_keys = list(bd.bd.keys())

rounds = 0
user_win = True

def print_followers():
    print(f"Option A:followers: {first_option_followers} vs Option B: followers: {second_option_folowers}")


first_option_key = random.choice(bd_keys)

while user_win:

    second_option_key = random.choice(bd_keys)
    first_option_definition = bd.bd[first_option_key][0]
    second_option_definition = bd.bd[second_option_key][0]
    first_option_followers = bd.bd[first_option_key][1]
    second_option_folowers = bd.bd[second_option_key][1]

    print(f"Compare A: {first_option_key}, {first_option_definition}")
    print(art.vs)
    print(f"Against B: {second_option_key}, {second_option_definition}")

    user_option =input("Who has more followers? Type 'A' or 'B': ").strip().upper()
    if user_option == "A":
        if first_option_followers > second_option_folowers:
            rounds += 1
            print(f"You win! Current round: {rounds}")
            print_followers()
            print("*"*20)
            print("*"*20+"Next Round"+"*"*20)  
        else:
            print("You lose!")
            print_followers()
            print(f"Final score: {rounds}")
            user_win = False
    elif user_option == "B":
        if second_option_folowers > first_option_followers:
            rounds += 1
            print(f"You win! Current round: {rounds}")
            print_followers() 
            print("*"*20)
            print("*"*20+"Next Round"+"*"*20)
            first_option_key = second_option_key
        else:
            print("You lose!")
            print_followers()
            print(f"Final score: {rounds}")
            user_win = False


