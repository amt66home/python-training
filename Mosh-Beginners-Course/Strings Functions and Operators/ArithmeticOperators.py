print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3) # returns an integer
print(10 % 3) # modulus
print(10 ** 3) # to the power of (exponentiation), so returns 10 to the power of 3

x = 10
x = x + 3
print(x)

# augmented assignment operators
x = 10
x += 3 
print(x)

x = 10
x -= 3
print(x)

# Operator precedence follows BODMAS
# the order is:
# exponentiation **
# multiplication or division * or /
# addition or subtraction + or -
x = 10 + 3 * 2 ** 2
print(x)

# use parenthesis to control the flow of operations
x = (2 + 3) * 10 - 3
print(x)
