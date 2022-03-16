numbers = [5,2,1,7,4]

# add a number to the end of the list
numbers.append(20)
print(numbers)

# add a number to a specific location in the list
numbers.insert(1,10)
print(numbers)

# remove a number
numbers.remove(5)
print(numbers)

# remove all items
numbers.clear()
print(numbers)

# remove last number in list
numbers = [5,2,1,7,4]
numbers.pop()
print(numbers)

# check for existence of an item, pass a value to get it's index
# if you pass a number that doesn't exist you get a value error
print(numbers.index(5))

# You can use 'in' to find an item in the list, will return true if
# it finds the item and false if it doesn't
print(50 in numbers)

# count the occuranc of an item
numbers = [5,2,1,7,4,5]
print(numbers.count(5))

# sort a list, doesn't return a value, just sorts the list
# to print the sorted list, sort it then print it
numbers.sort()
print(numbers)

# to sort in descending order
numbers.reverse()
print(numbers)

# copy the list
numbers = [5,2,1,7,4,5]
numbers2 = numbers.copy()
print(numbers2)

# remove duplicates in a list
mylist = [1,3,5,7,9,7,5]
uniques = []
for number in mylist:
    if number not in uniques:
        uniques.append(number)
print(uniques)








