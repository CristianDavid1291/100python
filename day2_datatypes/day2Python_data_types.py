bill = input ("What was the total bill? $")
tip = input ("What percentage tip would you like to give? 10, 12, or 15? ")
people = input ("How many people to split the bill? ")

# Calculate the total bill with tip
total_bill = float(bill) * (1 + float(tip) / 100)
# Calculate the amount each person should pay
amount_per_person = total_bill / int(people)
# Format the result to 2 decimal places
amount_per_person = round(amount_per_person,2)
# Print the result
print(f"Each person should pay: ${amount_per_person}")
