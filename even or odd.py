#WAP to check weather the given number is even or odd

#getting the number from the user
num=int(input("Enter the number: "))

#checking the given number is even or odd 
if num % 2 == 0 :
    #if given num is divisible by 2 and ==0 ,then it will print "the number is even" 
    print(" the number is even")
else :
     #if given num is divisible by 2 and it's not ==0 ,then it will print "the number is odd"
    print(" the number is odd")
