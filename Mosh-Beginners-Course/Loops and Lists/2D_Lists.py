matrix = [
    [1,2,3],
    [3,4,5],
    [6,7,8]
]
# return number 2
print(matrix[0][1])

# change the 2 to 20
matrix[0][1] = 20
print(matrix[0][1])

# iterate over the matrix
myNumbers = [
    [1,2,3],
    [3,4,5],
    [6,7,8]
]
for row in myNumbers:
    for item in row:
        print(item)

