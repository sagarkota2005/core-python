#WAP to get table of a number using function
def display_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Taking input from the user
num = int(input("Enter a number to get its table: "))
display_table(num)
