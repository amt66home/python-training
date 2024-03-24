# Python makes use of blocks:
block_head:
    1st block line
    2nd block line
    ...

# Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. 
# For example:
def my_function():
    print("Hello from My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

# Functions may return a value to the caller, using the keyword- 'return' . 
# For example:
def sum_two_numbers(a, b):
    return a + b

# To call a function write it's name followed by
# (), placing any required arguments in the brackets.

# Define our 3 functions
def my_function():
    print("Hello from My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
 
 def sum_two_numbers(a, b):
    return a + b

# printa simple greeting)
my_function()

# prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year")

# after this line x will the value 3!
x = sum_two_numbers(1,2)

# Exercise
# In this exercise you'll use an existing function, and while adding your own to create a fully functional program.
# Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", 
# "Easier code reuse", "Allowing programmers to share and connect code together"
# Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence 
# starting with the given string and ending with the string " is a benefit of functions!"

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organised code", "More readable code" , "Easier code reuse",
"Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(Benefit):
    return "%s is a benefit of functions!" % Benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
