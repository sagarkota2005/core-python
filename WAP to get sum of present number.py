num=int(input("enter the number: "))
sum1=0
rem=0
while(num>0):
     rem=num%10
     sum1=sum1+rem
     num=num//10
print("Sum of digit :",sum1)
