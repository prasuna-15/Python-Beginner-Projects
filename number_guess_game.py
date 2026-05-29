import random

secret_number = random.randint(1, 100)

attempts = 5

print("Welcome to Number Guessing Game")
print("Guess a number between 1 and 100")
print("You have", attempts, "attempts")

while attempts > 0:

    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

    attempts -= 1
    print("Remaining attempts:", attempts)

if attempts == 0:
    print("Game Over!")
    print("The correct number was:", secret_number)