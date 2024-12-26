# Simple Interest Calculation

# Fixed interest rate
interest_rate = 7

# Getting the principal_amount and duration from the user
principal_amount = float(input("Enter the principal amount: "))
duration = float(input("Enter the duration in years: "))

# Calculate simple interest
simple_interest = (principal_amount * interest_rate * duration) / 100

# Calculatting the total amount (principal_amount + interest)
total_amount = principal_amount + simple_interest

# Display the results
print(f"\nSimple Interest: {simple_interest}")
print(f"Total Amount after {duration} years: {total_amount}")
