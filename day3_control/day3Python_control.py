print("Welcome to rollercoaster! ")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("you can ride")
    age = int(input("What is your age? "))
    if age < 12:
        print("Ticket price is $7")
    elif age >= 12 and age < 18:
        print("Ticket price is $7")
    else:
        print("Ticket price is $12")

else:
    print("you can't ride")
  