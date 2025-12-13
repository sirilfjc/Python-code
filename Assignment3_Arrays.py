# program to demonstrate the sum of array elements
arr = [10, 20, 30, 40]
total = 0

for i in arr:
    total = total + i

print("Sum of array elements:", total)


# program to find average of array elements
arr = [10, 21, 32, 43, 54]
total = 0
count = 0

for i in arr:
    total = total + i
    count = count + 1

average = total / count
print("Average:", average)

# program to find index of a specific element in an array
arr = [1, 3, 5, 3, 1, 2, 6]
search = 3
index = 0
found = False

for i in arr:
    if i == search:
        print("Index of", search, "is", index)
        found = True
        break
    index = index + 1

if not found:
    print("Element not found")

# program to check if array contains a specific element
arr = [4, 5, 45, 40, 50]
search = 5
found = False

for i in arr:
    if i == search:
        found = True

if found:
    print("Element exists")
else:
    print("Element does not exist")

# program to remove specific element from array
arr = [44, 55, 0, 15, 19]
remove = 0
new_arr = []

for i in arr:
    if i != remove:
        new_arr.append(i)

print("Array after removal:", new_arr)

# program to implement copy of array
arr = ['k', 'a', 's', 'h', 'i']
copy_arr = []

for i in arr:
    copy_arr.append(i)

print("Copied array:", copy_arr)

# program to insert element at specific position in array
arr = [101, 303, 404, 505]
new_arr = []
insert = 202
pos = 1
index = 0

for i in arr:
    if index == pos:
        new_arr.append(insert)
    new_arr.append(i)
    index = index + 1

print("After insertion:", new_arr)

#program to find min and max element in an array
arr = [100, 3, 3000, 20, 500]

min_val = arr[0]
max_val = arr[0]

for i in arr:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print("Minimum:", min_val)
print("Maximum:", max_val)

# program to reverse an array
arr = [9, 8, 7, 6, 5]
rev = []
index = 0

for i in arr:
    index = index + 1

while index > 0:
    rev.append(arr[index - 1])
    index = index - 1

print("Reversed array:", rev)

# program to remove duplicate elements in an array
arr = [11, 22, 33, 11, 44]
unique = []

for i in arr:
    found = False
    for j in unique:
        if i == j:
            found = True
    if not found:
        unique.append(i)

print("Array without duplicates:", unique)

# program to count even and odd numbers in an array
arr = [1,2,3,4,5,6,7,8,9]
even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even:", even)
print("Odd:", odd)

# program to find the difference between 2 minimum elements in an array
arr = [10, 6, 11, 13, 14]
min_val = arr[0]
max_val = arr[0]

for i in arr:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print("Difference:", max_val - min_val)

# program to find if 12 and 23 are present in an array
arr = [1, 12, 19, 23, 33]
found12 = False
found23 = False

for i in arr:
    if i == 12:
        found12 = True
    if i == 23:
        found23 = True

if found12 and found23:
    print("Both 12 and 23 exist")
else:
    print("Both not present")

