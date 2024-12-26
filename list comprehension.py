#list comprehension.
marks=[20,35,50,78,40]
new_marks=[] #empty list
for x in marks:
    new_marks.append(x+2)
print(new_marks)

marks1={39,25,21,56,75}
new_marks1={x+2 for x in marks1}
print(new_marks1)
