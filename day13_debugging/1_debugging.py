import random

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item + 1
        new_item += random.randint(1, 10)
        b_list.append(new_item)
    return b_list

mutated_list = mutate([1, 2, 3, 4, 5])
print(mutated_list)