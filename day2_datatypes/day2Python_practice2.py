phrase = input("write a phrase: ")

special_characters = {'@', '$', '%', '!', '#'}

# Evaluación de la línea
result = ''.join([char for char in phrase if char not in special_characters])
result2  = "-".join(special_characters)

print(result)
print(result2)