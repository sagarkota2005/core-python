import random

# Generating a random number between 10 and 20
random_number = random.randint(10, 20)

# Give the user three chances to guess
for attempt in range(3):
    try:
       
        user_guess = int(input(f"Attempt {attempt + 1}/3: Enter a number between 10 and 20: "))

        if user_guess < random_number:
            print("Too Low!")
        elif user_guess > random_number:
            print("Too High!")
        else:
            print("\nCongratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number!")

    # If the user hasn't guessed correctly by the last attempt
    if attempt == 2 and user_guess != random_number:
        print(f"Sorry, you lost! The correct number was {random_number}.")
