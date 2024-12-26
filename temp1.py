units=int(input("enter the number of units consummed: "))

if units > 0 and units <= 100 :
    bill=units * 10
    print("your electricity bill is :",bill)
elif units >100 and units <= 200 :
     bill=100 * 10 + (units-100)* 15
     print("your electricity bill is :",bill)
elif units > 200 and units <=300 :
     bill=100 * 10 + 100 * 15 + (units-200) * 20
     print("your electricity bill is :",bill)
else :
     bill=100 * 10 + 100 * 15 + 100 * 20 + (units-300) * 25
     print("your electricity bill is :",bill)
