names = ['John','Bob','Mosh','Sarah','Mary']
print(names[-2])

# return all items starting at index 2
print(names[2:])

# return all items starting at index 2 and ending on index 3
print(names[2:4])

# return all items
print(names[:])

# to change a value in the list, make John Jon
names = ['John','Bob','Mosh','Sarah','Mary']
names[0] = 'Jon'
print(names)

# create a list of numbers and then find largest
numbers = [1,2,45,3,4,5,6]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
# or
print(max(numbers))
