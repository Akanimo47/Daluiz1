print("Welcome to the word guessing game!")
print()

secret_word = "mosiah"
secret_word2 = "ether"
count = 1
guess = input("What is your guess? ")
print()

while guess != secret_word:
    print("Your guess was not correct.")
    guess = input("What is your guess? ")
    count += 1
print("Congratulations! You guessed it!")
print(f"It took you {count} guesses.")

print()

question = input("Would you like to guess another word? ")
if question == "yes":
    print()
    guess2 = input("What is your guess? ")
    while guess2 != secret_word2:
        print("Your guess was not correct.")
        guess2 = input("What is your guess? ")
        count += 1
    print()
    print("Congratulations! You guessed it!")
    print(f"It took you {count} guesses.")
    print()
else:
    print("Thanks and goodbye")