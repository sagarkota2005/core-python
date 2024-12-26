#WAP to find weather person is eligible to vote or not.

#getting the age of the user
user_age = int(input("Enter your age: "))

#using if-else statement for checking user is eligible for vote or not
if(user_age >= 18):
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")
