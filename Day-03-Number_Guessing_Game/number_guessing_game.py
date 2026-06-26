
# Number Guessing Game
# Day 03 Python Project

import random

print("=" * 45)
print("      🎯 NUMBER GUESSING GAME")
print("=" * 45)

print("\nI have selected a number between 1 and 100.")
print("Can you guess it?\n")

# Generate a random number
secret_number = random.randint(1, 100)

attempts = 0

while True:

    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("📉 Too Low! Try Again.\n")

    elif guess > secret_number:
        print("📈 Too High! Try Again.\n")

    else:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print("Total Attempts:", attempts)
        break
