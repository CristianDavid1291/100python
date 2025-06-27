dictionary = {
    "Bug":"definition of bug",
    "Function":"definition of function",
    "Variable":"definition of variable"
    }

for key in dictionary:
    print(f"{key}: {dictionary[key]}")

dictionary2 = {
    "France":["Paris", "Lyon", "Marseille"],
    "Germany":["Berlin", "Munich", "Hamburg"]
}

#print Lyon
print(dictionary2["France"][1])

dictionary3 = {
    "France":["Paris", "Lyon", "Marseille"],
    "Germany":["Berlin", "Munich", "Hamburg"],
    "Italy": {
        "Cities": ["Rome", "Milan", "Naples"],
        "Population": [2873000, 1352000, 962000]
    }
}

print(dictionary3["Italy"]["Cities"][0])  # Rome

