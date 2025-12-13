# ---------------- EXCEPTION HANDLING EXAMPLE 1 ----------------

# Creating a list with three elements
a = [1, 2, 3]

# try block contains code that may cause an exception
try:
    # Accessing the second element of the list (valid index)
    print("Second element =", a[1])

    # Trying to access the fourth element
    # This will cause IndexError because index 3 does not exist
    print("Fourth element =", a[3])

# except block executes when any error occurs in try block
except:
    # Handles the error and prevents program from crashing
    print("An error occurred")


# Printing a blank line for better readability
print()


# ---------------- EXCEPTION HANDLING WITH ELSE BLOCK ----------------

# Creating another list
b = [3, 2, 1]

# try block for comparing two lists
try:
    # This comparison does NOT raise an exception
    # It simply returns True or False
    a == b

# except block executes only if an exception occurs
except:
    print("They are not equal")

# else block executes when NO exception occurs in try block
else:
    print("Both Equal")


# Printing a blank line
print()


# ---------------- EXCEPTION HANDLING WITH FINALLY BLOCK ----------------

# try block with code that causes ZeroDivisionError
try:
    # Dividing a number by zero (not allowed)
    k = 5 / 0
    print(k)

# except block catches a specific exception (ZeroDivisionError)
except ZeroDivisionError:
    print("Can't divide by zero")

# finally block always executes
# Used for cleanup operations like closing files, releasing resources
finally:
    print("This is always executed")
