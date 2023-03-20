# Tuples are like lists except you cannot amend them, they are
# immutable ie we cannot mutate or change them.
# We use square braces for lists and brackets for tuples
numbers = (1,2,3)
print(numbers[0])

# Tuples are useful if you want a list that cannot be accidentally changed

# Unpacking:
# lets say we want to assign values to x,y and z
coordinates = (1,2,3)
coordinates[0] * coordinates[1] * coordinates[2]

# You can store them in different variables
coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

print(x * y * z)

# you can also use unpacking for assigning values from a tuple
coordinates = (1,2,3)
x, y, z = coordinates
print(y)

