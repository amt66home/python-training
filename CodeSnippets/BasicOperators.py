from math import remainder


number = 1 + 2 * 3 / 4
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

hellowworld = "hello" + " " + "world"
print(hellowworld)

lotsofhellow = "hello" * 10
print(lotsofhellow)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3]*3)

# The target of this exercise is to create two lists called 
# x_list and y_list, which contain 10 instances of the variables 
# x and y, respectively. You are also required to create a list 
# called big_list, which contains the variables x and y, 10 times each, 
# by concatenating the two lists you have created.
# I have changed the code by adding an extra if statement that checks
# and if either list is not equal 10 then it prints "Wrong"

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 15
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
if big_list.count(x) != 10 or big_list.count(y) != 10:
    print("Wrong")




