#creating a dictionary in python
'''a dictionary0

'''
#creating a dictionary named my_dict
my_dict = {
    "std_id" :111,
    "std_name" :"Sagar",
    "course" : "BCA"
    }

print(my_dict)

x=my_dict["course"]
print("the course selected is ",x)

x=my_dict.get("std_id")
print(x)

#find all the keys presente in the dictionary
y=my_dict.keys()
print("the keys present are :",y)

#to update a element
my_dict.update({"std_name":"Sameer"})
print(my_dict)

#to add new element in the dictionary
my_dict["std_address"]= "badhlapur"
print(my_dict)

my_dict["fees"]= 53000
print(my_dict)

#to remove certain element from the dictionary
my_dict.popitem()
print(my_dict)


for i in my_dict.values():
    print(i)


for i in my_dict.keys():
    print(i)


for x,y in my_dict.items():
    print(x,y)


