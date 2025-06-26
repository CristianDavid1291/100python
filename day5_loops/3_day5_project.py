import random

print("Welcome to the Password Generator!")
letters_number = int(input("How many letters would you like in your password?"))
symbols_number = int(input("How many symbols would you like in your password?"))
numbers_number = int(input("How many numbers would you like in your password?"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

paswword_list = []

for letter in range(0, letters_number):
    paswword_list.append(random.choice(letters))
for symbol in range(0, symbols_number):
    paswword_list.append(random.choice(symbols))
for number in range(0, numbers_number):
    paswword_list.append(random.choice(numbers))
random.shuffle(paswword_list)
new_password = "".join(paswword_list)
print(new_password)


