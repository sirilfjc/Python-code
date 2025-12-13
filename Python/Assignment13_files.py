# Program to demonstrate reading and writing files in Python

# ----------------------------------------------------
# Reading data from a text file
# ----------------------------------------------------

# Open the file "HW.txt" in read mode ('r')
file1 = open("HW.txt", "r")

# Read the entire content of the file
data = file1.read()

# Print the content of the file
print(data)
print()   # Prints a blank line for readability

# Close the file after reading (good practice)
file1.close()


# ----------------------------------------------------
# Writing data into a text file
# ----------------------------------------------------

# Open the file "Blank.txt" in write mode ('w')
# If the file does not exist, it will be created
# If it exists, its content will be overwritten
file2 = open("Blank.txt", "w")

# String to be written into the file
str1 = 'Python'

# Write the string into the file
file2.write(str1)

print()   # Blank line

# Close the file after writing
file2.close()


# ----------------------------------------------------
# Reading file using read and write mode ('r+')
# ----------------------------------------------------

# Open the file "HW.txt" in read + write mode
file3 = open("HW.txt", "r+")

# Read only the first 11 characters from the file
print(file3.readline(11))

print()   # Blank line

# Close the file
file3.close()
