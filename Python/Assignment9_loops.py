# --------------------------------------------------
# 1. Print "Bright IT Career" ten times using for loop
# --------------------------------------------------

message = "Bright IT Career"

for i in range(10):
    print(message)

print("\n" + "-"*40 + "\n")


# --------------------------------------------------
# 2. Print numbers from 1 to 20 using while loop
# --------------------------------------------------

num = 1
while num <= 20:
    print(num, end=" ")
    num += 1

print("\n\n" + "-"*40 + "\n")


# --------------------------------------------------
# 3. Equal (==) and Not Equal (!=) operators
# --------------------------------------------------

a = 5
b = 10

print("a == b :", a == b)   # Equal operator
print("a != b :", a != b)   # Not equal operator

print("\n" + "-"*40 + "\n")


# --------------------------------------------------
# 4. Print even and odd numbers from a list
# --------------------------------------------------

numbers = [1,2,3,4,5,6,7,8,9,10]

print("Even Numbers:")
for i in numbers:
    if i % 2 == 0:
        print(i, end=" ")

print("\nOdd Numbers:")
for i in numbers:
    if i % 2 != 0:
        print(i, end=" ")

print("\n\n" + "-"*40 + "\n")


# --------------------------------------------------
# 5. Find the largest number among three numbers
# --------------------------------------------------

x = 40
y = 50
z = 90

if x >= y and x >= z:
    largest = x
elif y >= x and y >= z:
    largest = y
else:
    largest = z

print("Largest number is:", largest)

print("\n" + "-"*40 + "\n")


# --------------------------------------------------
# 6. Print even numbers between 10 and 20 using while
# --------------------------------------------------

start = 10
end = 20

print("Even numbers between 10 and 20:")
while start <= end:
    if start % 2 == 0:
        print(start, end=" ")
    start += 1

print("\n\n" + "-"*40 + "\n")


# --------------------------------------------------
# 7. Print numbers from 1 to 10 using do-while style
# --------------------------------------------------
# Python does not have do-while, so we simulate it

i = 1
print("Print 1 to 10 using do-while style loop:")
while True:
    print(i, end=" ")
    i += 1
    if i > 10:
        break

print("\n\n" + "-"*40 + "\n")


# --------------------------------------------------
# 8. Check whether a number is an Armstrong number
# --------------------------------------------------

num = int(input("Enter a number to check Armstrong: "))
temp = num
arm_sum = 0

while temp > 0:
    digit = temp % 10
    arm_sum += digit ** 3
    temp //= 10

if num == arm_sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

print("\n" + "-"*40 + "\n")


# --------------------------------------------------
# 9. Check whether a number is prime
# --------------------------------------------------

number = int(input("Enter a number to check Prime: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")

print("\n" + "-"*40 + "\n")


# --------------------------------------------------
# 10. Check whether a number is Palindrome
# --------------------------------------------------

num = int(input("Enter a number to check Palindrome: "))
temp = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if temp == reverse:
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")

print("\n" + "-"*40 + "\n")


# --------------------------------------------------
# 11. Check whether a number is EVEN or ODD
# --------------------------------------------------

num = int(input("Enter a number to check EVEN or ODD: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
