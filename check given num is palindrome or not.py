#WAP TO CHECK weather the given number is palindrome or not
#palindromes are like if given num is 343 and after reversing num is same as 343 then it called as palindrome

num = int(input("Enter a number:"))
temp=num
rev = 0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(rev==temp):
    print("given number is palindrome")
else:
    print("given number is not palindrome")
