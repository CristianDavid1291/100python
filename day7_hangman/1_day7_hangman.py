import random
words = ["python", "java", "javascript", "hangman", "programming", "developer", "code", "function", "variable", "loop",
         "condition", "syntax", "debugging", "algorithm", "data", "structure"]
word = random.choice(words)

print(f"{word}, {len(word)} letters")

print("Welcome to Hangman!")
print("You have 6 attempts to guess the word.")
print (f"Word: {len(word)} letters: {'_' * len(word)}")
print(word)
attempts = 6
guessLetters = []

def display_word(word, guessLetters):
    displayed = "".join(letter if letter in guessLetters else "_" for letter in word)
    return displayed
   
while attempts > 0:
    guessLetter = input("Guess a letter: ").lower()
    if guessLetter in word:
        print(f"Good guess! '{guessLetter}' is in the word.")
        guessLetters.append(guessLetter)
        if set(guessLetters) == set(word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
        else:
         print(f"Current word: {display_word(word, guessLetters)}")
    else:
        attempts -= 1
        print(f"Sorry, '{guessLetter}' is not in the word. You have {attempts} attempts left.") 
if attempts == 0:    
    ultimate_guess = input("Final attempt to guess word ").lower()
    if ultimate_guess == word:
        print(f"Congratulations! You've guessed the word: {word}") 
    else:
        print(f"Sorry, the word was: {word}. Better luck next time!")