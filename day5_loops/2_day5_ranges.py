
for number in range(1,10,3):
    print(number)

# range for fibonacci sequence
fibonacci = [0, 1]
for i in range(2, 10):
    next_number = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_number)   
print(fibonacci)
