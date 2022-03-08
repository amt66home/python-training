# Calculate length of string
course = 'Python for beginners'
print(len(course))

# We can use len to stop a user typing too many characters into a box
# It is not restricted to counting strings, eg it can also count items in a list
# It is a general purpose function, ie not tied to a type such as string.
# Functions tied to a type are called methods and can be accessed by typing the variable name
# followed by a dot
course = 'Python for beginners'
print(course.upper())
print(course.lower())
print(course.title())
 
print(course.find('P')) # find will get the index of the char to pass into it, note it is case sensitive
print(course.find('beginners')) # will return the index where the word beginners starts
print(course.replace('beginners','Absolute Beginners')) # replaces beginners with Absolute Beginners - is case sensitive
print(course.replace('P','J')) # will replace capital P with capital J

# check for a sequence of characters - returns true or false
course = 'Python for beginners'
print('Python' in course)




