#creating a function named check_voting_eligibility
def check_voting_eligibility(age):

    if age >= 18:
#if age is greater than 18 or equals then if statement will execute
        return "You are eligible to vote."
    else:
#if age is not greater than 18 or equals then else statement will execute
        return "You are not eligible to vote."

# Taking input from the user
age = int(input("Enter your age: "))
result = check_voting_eligibility(age)
print(result)
