
tuple1=("sagar",60,"o Grade",50000,"bhiwandi")
print(tuple1)
print(type(tuple1))

#tuple slicing
print(tuple1[1: ])
print(tuple1[ :4])
print(tuple1[1:3])

#for reversing the tuple
print(tuple1[::-1])

#find length of the tuple
print("the length of the tuple is: ",len(tuple1))

#converting tuple to list for adding the elements
list2=list(tuple1)
print(list2)

list2[2]="A in sports"
print(list2)

