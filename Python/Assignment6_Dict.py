# Creating a dictionary named 'students'
# Keys are roll numbers and values are student names
students = {1: 'Ravi', 2: 'Sita', 3: 'Aman'}

# Printing the initial dictionary
print("Initial Dictionary:", students)


# Adding a new key-value pair to the dictionary
# Key 4 is added with value 'Neha'
students[4] = 'Neha'

# Printing dictionary after adding new element
print("After adding element:", students)


# Updating an existing value in the dictionary
# Key 2 already exists, so its value is updated from 'Sita' to 'Pooja'
students[2] = 'Pooja'

# Printing dictionary after updating value
print("After updating value:", students)


# Accessing a value from the dictionary using its key
# Key 1 corresponds to the value 'Ravi'
print("Accessing value with key 1:", students[1])


# Deleting a key-value pair from the dictionary
# Key 3 and its value 'Aman' are removed
del students[3]

# Printing dictionary after deletion
print("After deleting element:", students)


# Creating a nested dictionary
# Dictionary inside another dictionary
student_info = {
    1: 'Ravi',      # Normal key-value pair
    2: {            # Nested dictionary
        'Age': 20,
        'Course': 'BSc',
        'Year': 'Second Year'
    }
}

# Printing the nested dictionary
print("Nested Dictionary:", student_info)


# Accessing a value from the nested dictionary
# First key 2, then inner key 'Age'
print("Accessing nested Age:", student_info[2]['Age'])
