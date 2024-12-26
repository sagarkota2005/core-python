# Create an empty list with the named dynamic_list
dynamic_list = []

# Ask the user to input 5 elements
for i in range(5):
    element = input(f"Enter element {i + 1}: ")
    dynamic_list.append(element)

print("Initial List:", dynamic_list)

# Perform insert operation
new_element = input("Enter a new element to insert: ")
position = int(input(f"Enter position (0 to {len(dynamic_list)}): "))
dynamic_list.insert(position, new_element)
print("List after insertion:", dynamic_list)

# Perform delete operation
delete_element = input("Enter the element to delete: ")
if delete_element in dynamic_list:
    dynamic_list.remove(delete_element)
else:
    print(f"Element '{delete_element}' not found in the list.")
print("List after deletion:", dynamic_list)
