astring = "Hello world!"
print("single quotes are ' ' ")

print(len(astring))

# This returns the index of the first o in the string
# It returns 4 because it starts at 0
astring = "Hello world!"
print(astring.index("o"))

# Return count of the letter l
string = "Hello world!"
print(astring.count("l"))

# This prints a slice of the string, starting at index 3, and ending at index 6. 
# But why 6 and not 7? Again, most programming languages do this - it makes doing 
# math inside those brackets easier.
# If you just have one number in the brackets, it will give you the single character 
# at that index. If you leave out the first number but keep the colon, it will give 
# you a slice from the start to the number you left in. If you leave out the second 
# number, it will give you a slice from the first number to the end.
# You can even put negative numbers inside the brackets. They are an easy way of 
# starting at the end of the string instead of the beginning. This way, -3 means 
# "3rd character from the end".
string = "Hello world!"
print(astring[3:7])

# This prints the characters of string from 3 to 7 skipping one character. 
# This is extended slice syntax. The general form is [start:stop:step].
string = "The quick brown fox"
print(astring[3:7:2])

# Note that both of them produce same output
#There is no function like strrev in C to reverse a string. 

astring = "The quick brown fox"
print(astring[3:7])
print(astring[3:7:1])
print(astring[3:7:4])

# But with the above mentioned type of slice syntax you can easily reverse a string 
# like this
astring = "The quick brown fox"
print(astring[::-1])

astring = "The quick brown fox"
print(astring.upper())
print(astring.lower())

# This is used to determine whether the string starts with something or ends with 
# something, respectively. The first one will print True, as the string starts with 
# "Hello". The second one will print False, as the string certainly does not end with 
# "asdfasdfasdf".
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# This splits the string into a bunch of strings grouped together in a list. 
# Since this example splits at a space, the first item in the list will be "Hello", 
# and the second will be "world!".
astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)

# do the excercise
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))



