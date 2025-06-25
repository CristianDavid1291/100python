print("Welcome to Python Pizza Delivery!")
size = input("What kind of pizza do you want? S, M or L? ")
add_pepperoni = input("Do you want to add pepperoni? Y or N? ")
extra_cheese = input("Do you want to add extra cheese? Y or N? ") 

bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2

elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3

elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")
