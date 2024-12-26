#sorting the values as descending order and returning the secound largest value in the list
marks = [23,34,56,92,65]

#here we are 
for i in range(0,5):
    for j in range(i+1,5):
        if marks[j]>marks[i]:
            temp=marks[i]
            marks[i]=marks[j]
            marks[j]=temp

print(marks)
print(marks[1])
