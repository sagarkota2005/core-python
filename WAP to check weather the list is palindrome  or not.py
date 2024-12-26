
l2=[22,76,94,34,67,32,33]
temp=list(set(l2))
rev = 0
while(l2[] > 0):
    rem=l2%10
    rev=rev*10+rem
    l2=l2//10
if(rev==temp):
    print("given number is palindrome")
else:
    print("given number is not palindrome")
