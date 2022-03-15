# generate a list of coordinates

# generate the x values
for x in range(4):
    print(x)

# now generate a y value for each x value
# the y value will go up to 2 then start again
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

# print out x'x to make the letter F
numbers = [5,2,5,2,2]

for x_count in numbers:
    # result = letter * int(y) 
    result = ''
    for count in range(x_count):
        result += 'x'
    print(result)

# or you could do it this way
for x_count in numbers:
    print('x' * x_count)
