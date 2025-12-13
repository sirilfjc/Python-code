# ---------------------------------------------
# 1. Function for arithmetic operations (+, -, *, /)
# ---------------------------------------------

def arithmetic_operations(num1, num2):
    """
    This function performs basic arithmetic operations
    such as addition, subtraction, multiplication, and division.
    """
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2

    # Division needs zero check
    if num2 != 0:
        div = num1 / num2
    else:
        div = "Cannot divide by zero"

    # Display results
    print("Addition:", add)
    print("Subtraction:", sub)
    print("Multiplication:", mul)
    print("Division:", div)


# Taking input from user
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

arithmetic_operations(n1, n2)

print("\n---------------------------------------------\n")

# ---------------------------------------------
# 2. Increment and Decrement operations
# ---------------------------------------------

# Increment operation
a = 0
a += 1           # Increment by 1
a = a + 1        # Increment by 1 again
print("Value after increment:", a)

# Increment using for loop
print("\nIncremented for loop:")
for i in range(0, 5):   # Default step is +1
    print(i)

# Decrement using for loop
print("\nDecremented for loop:")
for i in range(4, -1, -1):   # Step is -1
    print(i)

print("\n---------------------------------------------\n")

# ---------------------------------------------
# 3. Check whether two numbers are equal or not
# ---------------------------------------------

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if x == y:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")

print("\n---------------------------------------------\n")

# ---------------------------------------------
# 4. Relational operators demonstration
# ---------------------------------------------

a = 4
b = 5

print("a < b  :", a < b)
print("a <= b :", a <= b)
print("a > b  :", a > b)
print("a >= b :", a >= b)
print("a == b :", a == b)
print("a != b :", a != b)

print("\n---------------------------------------------\n")

# ---------------------------------------------
# 5. Find smaller and larger number
# ---------------------------------------------

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Finding larger number
if num1 > num2:
    print(num1, "is the larger number")
else:
    print(num2, "is the larger number")

# Finding smaller number
if num1 < num2:
    print(num1, "is the smaller number")
else:
    print(num2, "is the smaller number")
