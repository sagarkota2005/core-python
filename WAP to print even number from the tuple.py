
'''WAP to print even number from the tuple
'()' round brackets for tuple, '[]' for list,'{}' curly braces for set,
'{}' for dictionary also it idetifies dictionary with key:value pair
'''
tuple1=(11,23,43,56,77,33,45,22,67,9,45,21)

for i in tuple1:
    if i%2==0:
        print(i)

print("the 45 occurs in the tuple:",tuple1.count(45),
