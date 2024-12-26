#accept the percentage from the user and make decision about is grade\

userPercentage=int(print("ENTER your percentage: "))

if userPercentage >=70 :
    print("your grade is O")
elif userPercentage >=60 :
     print("your grade is A")
elif userPercentage >=40 :
     print("your grade is B")
elif userPercentage < 40 :
     print("you are fail")
else :
    print("enter the valid input")
