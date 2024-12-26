#Q.1)write a function to reverse a list without using the built-in reverse() method.

def rev_list(l):
    return l[::-1]
l=[12,33,55,65,77,89,96]
print("the reverse is:",rev_list(l))
