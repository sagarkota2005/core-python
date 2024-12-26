#creating the list1 and list2 with their elements
list1 = [1,2,5,7,3,71,34]
list2 = [43,2,6,33,71,21]

#printing the two lists, list1 and list2
print("list1 elements is:",list1)
print("list2 elements is:",list2)

# Perform intersection using set operations
intersection = list(set(list1) & set(list2))

#output of  two lists after intersection
print("Intersection of the two lists:", intersection)
