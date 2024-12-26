i=0
list1= list(input("enter the 8 emails:"))
for i in list1:
    if i <= 8 :
        list1=list1[i]
        print(f"list list1[i] is: ",list1[i])

list1 =set(list1)
print("after removing the duplicate emails from the list",list1)
