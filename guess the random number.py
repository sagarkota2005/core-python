import random

# Generating a random number between 10 and 30
random_number = random.randint(10, 30)

# Give the user three chances to guess
for attempt in range(3):
    try:

     # Take input from the user
        user_guess = int(input(f"Attempt {attempt + 1}/3: Enter a number between 10 and 30: "))
        
        if user_guess == random_number:
            print("You won!")
            break
        elif attempt < 2:
            print("Try again!")
        else:
            print(f"Sorry, you lost! The correct number was {random_number}.")
    except ValueError:
        print("Please enter a valid number!")
