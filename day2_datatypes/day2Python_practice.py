phrase = input("write a phrase: ")

# separate the phrase into parts by space

parts = phrase.split(" ")
invertPrhase = ""
for part in parts:
    # reverse each part
    invertPrhase += part[::-1] + " "

print(invertPrhase) 