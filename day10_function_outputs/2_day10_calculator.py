def calculator(first, operation, second):
    """Performs basic arithmetic operations."""
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        if second != 0:
            return first / second
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

while True:    
    first_number = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    second_number = float(input("Enter second number: "))

    result = calculator(first_number, operation, second_number)
    print(f"The result of {first_number} {operation} {second_number} is: {result}")

    continue_calculating = input(f"Type 'y' to continue with {result} or type 'n' to start a new calculation: ").strip().lower()
    while continue_calculating == 'y':
        operation = input("Enter operation (+, -, *, /): ")
        second_number = float(input("Enter second number: "))
        result = calculator(result, operation, second_number)
        print(f"The result of {result} {operation} {second_number} is: {result}")
        continue_calculating = input(f"Type 'y' to continue with {result} or type 'n' to start a new calculation: ").strip().lower()


