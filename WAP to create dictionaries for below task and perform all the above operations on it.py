def create_student_dictionary(student_data):
  """
  Creates a dictionary of students with their roll numbers as keys.

  Args:
    student_data: A list of tuples, where each tuple contains 
                  (roll_number, name, marks).

  Returns:
    A dictionary where keys are roll numbers and values are 
    dictionaries containing 'name' and 'marks' of the student.
  """
  student_dict = {}
  for roll_no, name, marks in student_data:
    student_dict[roll_no] = {'name': name, 'marks': marks}
  return student_dict

def get_student_details(student_dict, roll_no):
  """
  Retrieves the details of a student given their roll number.

  Args:
    student_dict: The dictionary of students.
    roll_no: The roll number of the student.

  Returns:
    A dictionary containing the 'name' and 'marks' of the student, 
    or None if the roll number is not found.
  """
  return student_dict.get(roll_no)

def update_student_marks(student_dict, roll_no, new_marks):
  """
  Updates the marks of a student given their roll number.

  Args:
    student_dict: The dictionary of students.
    roll_no: The roll number of the student.
    new_marks: The new marks of the student.

  Returns:
    True if the update was successful, False otherwise.
  """
  if roll_no in student_dict:
    student_dict[roll_no]['marks'] = new_marks
    return True
  return False

def delete_student(student_dict, roll_no):
  """
  Deletes a student from the dictionary given their roll number.

  Args:
    student_dict: The dictionary of students.
    roll_no: The roll number of the student.

  Returns:
    True if the deletion was successful, False otherwise.
  """
  if roll_no in student_dict:
    del student_dict[roll_no]
    return True
  return False

def display_all_students(student_dict):
  """
  Displays the details of all students.

  Args:
    student_dict: The dictionary of students.
  """
  for roll_no, student in student_dict.items():
    print(f"Roll No: {roll_no}, Name: {student['name']}, Marks: {student['marks']}")

# Example usage
student_data = [
    (1, "Alice", 85),
    (2, "Bob", 90),
    (3, "Charlie", 78),
]

student_dict = create_student_dictionary(student_data)

# Get student details
student_details = get_student_details(student_dict, 2)
print(f"Student Details (Roll No 2): {student_details}")

# Update student marks
if update_student_marks(student_dict, 1, 88):
  print("Marks updated successfully.")

# Delete student
if delete_student(student_dict, 3):
  print("Student deleted successfully.")

# Display all students
display_all_students(student_dict)
