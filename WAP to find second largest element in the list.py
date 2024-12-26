
#Q.2)WAP to find second largest number in a list
l2=[12,76,94,34,67,85,34]

remove_dup=(list(set(l2)))
print("the final list is :",remove_dup)

sorted_list =sorted(remove_dup)

print("the sorted list is :",sorted_list)
print("the second largest element is:",sorted_list[-2])
