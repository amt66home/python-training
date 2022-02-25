birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(age)

weight_lbs = input('What is your weight in pounds: ')
weight_kg = str(int(weight_lbs) *0.45)
print('Your weight in kg is: '+ weight_kg)

course = "Python's for Beginners"
print(course)

course_2 = 'Python for "Beginners"'
print(course_2)

course_3 = ''' 
Hi John,

Here is our first email to you.

Thank you,
The support team

'''
print(course_3)

course_2 = 'Python for Beginners'
print(course_2[0])

# if you use a negative index it will fetch from the end of the string
course_2 = 'Python for Beginners'
print(course_2[-1])

# You can return several characters. The index begins at 0. So this example
# will return the first three characters starting at index 0.
course_2 = 'Python for Beginners'
print(course_2[0:3])

# If you don't state how many characters it will return them all, so the following
# example will return thon for Beginners
course_2 = 'Python for Beginners'
print(course_2[2:])

# If you don't supply the start index it will default to 0
course_2 = 'Python for Beginners'
print(course_2[:5])

# If you don't provide any indexes it will use the defaults ie 0
course_2 = 'Python for Beginners'
print(course_2[:])

# We can create a copy of our variable
course_2 = 'Python for Beginners'
another = course_2[:]
print(another)

# The following will return all the characters from index 1 to 1 character from the end:
name = 'Jennifer'
print(name[1:-1])




