from functools import reduce


def cuadrado(entrada):
   square_entrada = map(lambda x: x ** 2, entrada)
   return list(square_entrada)

def filert_even(entrada):
    even_entrada = filter(lambda x: x % 2 == 0, entrada)
    return list(even_entrada)

def addition(entrada):
    sum_entrada = reduce(lambda x, y: x + y, entrada)
    return sum_entrada

def sort_in(entrada, num):
    min = filter(lambda x: x <= num, entrada)
    max = filter(lambda x: x > num, entrada)
    return list(min) + [num] + list(max)

def sort_list():
    entrada = [4, 8, 3, 1, 5]
    sorted_list = reduce(lambda x, y: sort_in(x, y), entrada, [])
    return sorted_list

def filter_double(entrada):
    final_list = list(map(lambda x: x * 2, list(filter(lambda x: x % 3 == 0, entrada))))
    return final_list

def longer(entrada):
    max_len = reduce(lambda x, y: x if len(x) > len(y) else y, entrada)
    return max_len

def concatenate(entrada):
    return reduce(lambda x, y: x + y, entrada)

def tranform(entrada):
    return list(map(lambda x: x.upper(), entrada))

def sum_positive(entrada):
    return reduce(lambda x, y: x + y if x >= 0 and y >= 0 else x, entrada, 0)

def list_lon(entrada):
    return list(map(lambda x: len(x), entrada))

def filter_vowel(entrada):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return list(filter(lambda x: x[0].lower() in vowels, entrada))

def filter_vowel2(entrada):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_list = ''.join(list(filter(lambda x: x not in vowels, entrada)))
    return new_list

# print(f"Square numbers: {cuadrado([1, 2, 3, 4, 5])}")
# print(f"Even numbers: {filert_even([1, 2, 3, 4, 5])}")
# print(f"Sorted list: {sort_list()}")
# print(f"filter double: {filter_double([1, 2, 3, 4, 5, 6, 7, 8, 9])}")
# print(f"longer: {longer(['apple', 'banana', 'cherry', 'date'])}")
# print(f"Concatenate: {concatenate(['Hello', ' ', 'World', '!'])}")
# print(f"Transform: {tranform(['hello', 'world'])}")
# print(f"Sum positive: {sum_positive([-1, -2, 3, -4, 5])}")
# print(f"List length: {list_lon(['apple', 'banana', 'cherry'])}")
# print(f"Filter vowel: {filter_vowel(['apple', 'banana', 'erry', 'ate'])}")
print(f"Filter vowel2: {filter_vowel2("applebananaerryate")}")




    