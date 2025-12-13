# Program to demonstrate static (class) variable in Python

class Python:
    # Static / Class variable
    # This variable belongs to the class, not to any object
    staticVariable = 9


# Accessing static variable using class name
print("Access through class:", Python.staticVariable)


# Modifying static variable using class name
Python.staticVariable = 12
print("After modifying through class:", Python.staticVariable)


# Creating an object (instance) of the class
instance = Python()

# Accessing static variable using object
# Object first checks its own variables, if not found it checks class variable
print("Access through instance:", instance.staticVariable)


# Modifying static variable using instance
# This creates a NEW instance variable, not changing class variable
instance.staticVariable = 15
print("After modifying through instance:", instance.staticVariable)


# Checking class variable again
# It remains unchanged because instance modification created a separate variable
print("Class variable remains:", Python.staticVariable)
