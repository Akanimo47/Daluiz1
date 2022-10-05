
import random


print("Welcome to the word guessing game!")
print()

name = input("Enter your Name: ")

words = ["mosiah", "ether", "mormon", "monson", "jesus", "savior"]

secret_word = random.choice(words)
number = len(secret_word)

count = 1
guess = input(f"Enter a {number} letters word: ").lower()
print()


while secret_word != guess:
    for i, char in enumerate(guess):
        if char.lower() == secret_word[i]:
            print(f"{char.upper()} ", end = "")


        # elif char.lower().find(secret_word) != secret_word.find(secret_word) and char.lower() in secret_word:
            # print(f"{char.lower()} ", end = "")
            

        elif char in secret_word:
            print(f"{char} ", end = "")
        else: 
            print(f"_ ", end = "")
       

    print("Your guess was not correct.")
    guess = input(f"Enter a {number} letters word: ").lower()
    count += 1
print(f"Congratulations {name.capitalize()}! You guessed it!\nThe word is {secret_word.upper()}!")
print(f"It took you {count} guesses.")

print()
