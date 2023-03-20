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

# You can use unpacking with lists:
numbers = [1,5,3]
a, b, c = numbers
print(b + a)

# Add a number to a list
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

# Add a number to a position 3 (index 2) in a list
numbers = [5, 2, 1, 7, 4]
numbers.insert(2, 10)
print(numbers)

# Remove an item from a list - remov the number 5
numbers = [5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)

# Remove all items from a list
numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

# Remove last item in the list
numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

# find the index of the first number 5 in the list
numbers = [5, 2, 1, 7, 5]
print(numbers.index(5))

# check for existence of number in a list, returns true or false
numbers = [5, 2, 1, 7, 5]
print(50 in numbers)

# count the incidences of a number in a list
numbers = [5, 2, 1, 7, 5]
print(numbers.count(5))

# sort list then print it
numbers = [5, 2, 1, 7, 5]
numbers2 = numbers.copy()
numbers.append(10)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)



