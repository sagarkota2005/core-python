
def factorial(num):
    if num < 0:
        return "Factorial does not exist for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        return fact

# Get input from the user
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")
